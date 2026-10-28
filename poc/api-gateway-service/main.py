"""
Servicio de API Gateway actual con problemas de acoplamiento.

Este servicio actúa como punto de entrada único para todas las solicitudes
de la plataforma logística, pero actualmente implementa lógica de negocio
que debería estar delegada a servicios especializados, creando acoplamiento
fuerte y dificultando la escalabilidad.

Problemas arquitectónicos presentes:
1. Acoplamiento directo a servicios internos (inventario, ruteo, tracking)
2. Lógica de orquestación en el gateway (debería ser responsabilidad de un orquestador)
3. Manejo de errores y reintentos hardcodeado
4. Falta de patrones de resiliencia (circuit breaker, retries)
5. Configuración de rutas estática

El candidato deberá:
- Identificar los problemas de acoplamiento
- Proponer una arquitectura desacoplada
- Implementar patrones de resiliencia
- Definir contratos claros entre componentes
"""

import asyncio
import json
from datetime import datetime
from typing import Dict, Any, Optional, List

import aiohttp
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(title="API Gateway - Plataforma Logística", version="1.0.0")

# Configuración hardcodeada de servicios (problema 1 y 5)
SERVICE_CONFIG = {
    "inventario": {
        "url": "http://inventario-service:8001",
        "endpoints": {
            "verificar_stock": "/api/inventario/verificar",
            "reservar": "/api/inventario/reservar"
        }
    },
    "ruteo": {
        "url": "http://ruteo-service:8002",
        "endpoints": {
            "calcular_ruta": "/api/ruteo/calcular",
            "optimizar": "/api/ruteo/optimizar"
        }
    },
    "tracking": {
        "url": "http://tracking-service:8003",
        "endpoints": {
            "crear_envio": "/api/tracking/envios",
            "actualizar_estado": "/api/tracking/envios/{envio_id}/estado"
        }
    },
    "notificaciones": {
        "url": "http://notificaciones-service:8004",
        "endpoints": {
            "enviar": "/api/notificaciones/enviar"
        }
    }
}

# Modelos de dominio (deberían estar en un paquete separado)
class Producto(BaseModel):
    id: str
    nombre: str
    cantidad: int
    ubicacion: str

class Pedido(BaseModel):
    id: str
    productos: List[Producto]
    cliente_id: str
    direccion_entrega: str
    prioridad: str
    fecha_creacion: datetime = datetime.now()

class Envio(BaseModel):
    id: str
    pedido_id: str
    ruta_id: str
    transportista_id: str
    estado: str = "CREADO"
    eventos: List[Dict[str, Any]] = []

class Ruta(BaseModel):
    id: str
    origen: str
    destino: str
    distancia_km: float
    tiempo_estimado: str
    puntos_intermedios: List[str]

# Cliente HTTP hardcodeado sin patrones de resiliencia (problema 4)
class ServicioCliente:
    def __init__(self, servicio_nombre: str):
        self.config = SERVICE_CONFIG[servicio_nombre]
        self.base_url = self.config["url"]

    async def post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.base_url}{self.config['endpoints'][endpoint]}"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=data) as response:
                    if response.status != 200:
                        raise HTTPException(
                            status_code=response.status,
                            detail=f"Error en {endpoint}: {await response.text()}"
                        )
                    return await response.json()
        except aiohttp.ClientError as e:
            raise HTTPException(
                status_code=503,
                detail=f"Servicio {self.config['url']} no disponible: {str(e)}"
            )

# Lógica de negocio en el gateway (problema 2)
class OrquestadorPedidos:
    def __init__(self):
        self.inventario = ServicioCliente("inventario")
        self.ruteo = ServicioCliente("ruteo")
        self.tracking = ServicioCliente("tracking")
        self.notificaciones = ServicioCliente("notificaciones")

    async def procesar_pedido(self, pedido: Pedido) -> Envio:
        """
        Flujo completo de procesamiento de pedido en el gateway:
        1. Verificar stock
        2. Reservar inventario
        3. Calcular ruta
        4. Crear envío
        5. Notificar cliente
        
        Problemas:
        - Toda la orquestación está acá (debería estar en un servicio dedicado)
        - Manejo de errores básico
        - Sin compensación de transacciones
        - Sin patrones de resiliencia
        """
        try:
            # 1. Verificar stock (lógica debería estar en inventario)
            productos_verificados = []
            for producto in pedido.productos:
                stock = await self.inventario.post("verificar_stock", {
                    "producto_id": producto.id,
                    "cantidad": producto.cantidad,
                    "ubicacion": producto.ubicacion
                })
                if not stock["disponible"]:
                    raise HTTPException(
                        status_code=400,
                        detail=f"Producto {producto.nombre} sin stock suficiente"
                    )
                productos_verificados.append(stock)

            # 2. Reservar inventario
            reserva = await self.inventario.post("reservar", {
                "productos": [
                    {"id": p.id, "cantidad": p.cantidad}
                    for p in pedido.productos
                ],
                "pedido_id": pedido.id
            })

            # 3. Calcular ruta (lógica debería estar en ruteo)
            ruta = await self.ruteo.post("calcular_ruta", {
                "origen": "CENTRAL",
                "destino": pedido.direccion_entrega,
                "peso_total": sum(p.cantidad for p in pedido.productos) * 0.5,  # kg
                "prioridad": pedido.prioridad
            })

            # 4. Crear envío
            envio_data = {
                "pedido_id": pedido.id,
                "ruta_id": ruta["id"],
                "transportista_id": "TRANS-DEFAULT",
                "productos": [
                    {"id": p.id, "cantidad": p.cantidad}
                    for p in pedido.productos
                ]
            }
            envio = await self.tracking.post("crear_envio", envio_data)

            # 5. Notificar cliente (lógica debería estar en notificaciones)
            await self.notificaciones.post("enviar", {
                "destinatario": pedido.cliente_id,
                "tipo": "pedido_confirmado",
                "contenido": {
                    "pedido_id": pedido.id,
                    "fecha_estimada": ruta["tiempo_estimado"],
                    "ruta_id": ruta["id"]
                }
            })

            return Envio(**envio)

        except HTTPException:
            # Compensación básica (problema 3 - debería ser más robusta)
            try:
                await self.inventario.post("reservar", {
                    "productos": [
                        {"id": p.id, "cantidad": -p.cantidad}
                        for p in pedido.productos
                    ],
                    "pedido_id": pedido.id
                })
            except Exception:
                pass
            raise

# Endpoints del API Gateway (deberían ser solo passthrough)
@app.post("/api/pedidos", response_model=Envio)
async def crear_pedido(pedido: Pedido, request: Request):
    """
    Endpoint para crear un pedido.
    
    Problemas:
    - Implementa lógica de negocio
    - Maneja transacciones de forma simplista
    - No valida datos de entrada correctamente
    - No tiene rate limiting
    - No implementa circuit breaker
    """
    orquestador = OrquestadorPedidos()
    try:
        return await orquestador.procesar_pedido(pedido)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error procesando pedido: {str(e)}"
        )

@app.get("/api/envios/{envio_id}", response_model=Envio)
async def consultar_envio(envio_id: str):
    """Endpoint para consultar estado de envío."""
    try:
        tracking = ServicioCliente("tracking")
        envio = await tracking.post(
            "crear_envio",  # Este endpoint debería ser GET /envios/{id}
            {"envio_id": envio_id}  # Problema: usando POST para consulta
        )
        return Envio(**envio)
    except HTTPException as e:
        raise e

@app.post("/api/envios/{envio_id}/cancelar")
async def cancelar_envio(envio_id: str):
    """Endpoint para cancelar un envío."""
    try:
        tracking = ServicioCliente("tracking")
        # Falta compensación de inventario al cancelar
        return await tracking.post(
            "actualizar_estado",
            {
                "envio_id": envio_id,
                "estado": "CANCELADO",
                "motivo": "Cancelación por usuario"
            }
        )
    except HTTPException as e:
        raise e

# Health check (único endpoint bien implementado)
@app.get("/health")
async def health_check():
    return {"status": "healthy", "services": list(SERVICE_CONFIG.keys())}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)