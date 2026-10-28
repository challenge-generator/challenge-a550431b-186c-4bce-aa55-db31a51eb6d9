# Prompt para Mejorar el Codigo Base

Copia y pega el contenido del bloque de abajo en un asistente de IA (Claude, ChatGPT)
para obtener un ZIP con el proyecto completo y arrancable.

Si preferis trabajar en tu editor con un agente local (Claude Code, Cursor, Copilot), usa `AGENTS.md` en vez de este archivo: dice lo mismo pero para que escriba los archivos en disco.

## Las dos reglas que no se negocian

1. **Completa el boilerplate.** Todo lo que el proyecto necesita para compilar y arrancar: manifiesto de dependencias, punto de entrada, configuracion, capa de interfaz, y las capas del patron arquitectonico declarado. Eso es andamiaje y es tu trabajo.
2. **NO resuelvas el reto.** Los entregables de las fases son el trabajo de la persona. El hueco pedagogico se deja como esta: el proyecto arranca, pero lo que el reto pide implementar NO esta implementado.

Dicho de otra forma: si algo impide compilar, arreglalo. Si algo es logica de negocio incompleta, validaciones ausentes, un secreto hardcodeado o un patron mejorable, dejalo exactamente como esta — es lo que la persona tiene que encontrar.

## Superficie de practica — NO resuelvas

Estos archivos SON el ejercicio de la persona. No los implementes; deja stubs.

- `adr/001-contexto-logistico.md` — El topic pide decisiones de arquitectura: el ADR es el ejercicio.
- `adr/002-diseno-arquitectonico.md` — El topic pide decisiones de arquitectura: el ADR es el ejercicio.

## Como saber que terminaste

```bash
python3 -c "import glob,sys; assert glob.glob('adr/*.md') and glob.glob('diagramas/*.mmd'), 'faltan ADRs o diagramas'"
```

Ese comando corriendo sin errores es la definicion de "listo".

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Perfil
Chapter Arquitectura, Especialidad Soluciones, Advanced

### Brecha de conocimiento
Entiende, aplica y sigue una metodología para el diseño de Arquitectura, toma decisiones de arquitectura y acompaña su salida a producción, comprende y aplica metodologías y framework como ADD, DDD y métodos de evaluación como ATAM y SAAM, también sabe usar event storming

### Misión / candidato
Candidato con experiencia aplicando DDD y ADD en arquitecturas complejas de microservicios, integraciones con sistemas legados, y evaluación de trade-offs arquitectónicos.

### Reto
- Tema: Metodologías y frameworks para diseño y evaluación de arquitectura de software
- Seniority: advanced-l3
- Tipo: mixed
- Título: Diseño y Evaluación de Arquitectura para Plataforma Logística
- Tiempo estimado: 180 minutos

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Facilitar Sesión de Event Storming — objetivo: Generar insights y eventos clave del dominio logístico — entregable (NO resolver): Mapa de eventos y procesos logísticos.
- Fase 2: Definir Mapa de Contextos con DDD — objetivo: Establecer los límites y contextos de la plataforma logística — entregable (NO resolver): Mapa de contextos DDD para la plataforma logística.
- Fase 3: Aplicar Iteraciones de Diseño con ADD 3.0 — objetivo: Iterar en el diseño de la arquitectura utilizando ADD 3.0 — entregable (NO resolver): Documento de diseño iterativo utilizando ADD 3.0.
- Fase 4: Realizar Evaluación Formal ATAM — objetivo: Documentar riesgos de rendimiento y escalabilidad — entregable (NO resolver): Informe de evaluación ATAM con hallazgos y recomendaciones.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 0 — ¿Esto es un proyecto o una carcasa?
Antes de extraer archivos, leé el Briefing (si está) y diagnosticá el adjunto.

Es CARCASA si ocurre CUALQUIERA de estas:
- No hay manifiesto de dependencias del stack del briefing (manifest.json de VTEX IO / package.json / pom.xml / build.gradle / requirements.txt / go.mod / *.tf / *.csproj, según corresponda)
- Hay un "binario" que en realidad es un comentario ("no puede ser mostrado como texto plano", placeholder .fig/.docx vacío)
- Los markdowns ya completan entregables de fases posteriores ("se implementó fade-in", lista de áreas ya resuelta)

Si es CARCASA:
- MATERIALIZÁ un proyecto que arranca en el stack del briefing (VTEX IO Store Framework, Angular, Terraform, pytest, Nest, etc.). Incluí manifiesto, punto de entrada y capa de interfaz reales.
- NO copies los markdowns de "solución" como si fueran el producto. Son ruido de generación.
- NO resuelvas las fases del briefing (están marcadas PROHIBIDO). Dejá el hueco pedagógico: el flujo existe, las microinteracciones/calidad/infra que el reto pide NO están hechas.
- Después seguí al PASO 5 (ZIP).

Si es un proyecto REAL (manifiesto + código que compila o arranca):
- Seguí PASO 1 en adelante. 🔴 compilación sí. 🟡 pedagógico no.

PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación, placeholders o binarios fake, NO la reproduzcas:
aplicá PASO 0 (materializar el proyecto del briefing). Reproducir la carcasa es un fallo.
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

// === ARCHIVO: poc/api-gateway-service/main.py ===
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

// === ARCHIVO: arquitectura.md ===
# Arquitectura de la Plataforma Logística

## Vistas de Arquitectura

### 1. Vista de Contexto
> Preguntas guía:
> - ¿Qué actores externos interactúan con la plataforma logística y qué información intercambian?
> - ¿Cuáles son los sistemas legados o externos que deben integrarse y qué protocolos de comunicación utilizan?
> - ¿Cómo se relacionan los dominios principales (gestión de pedidos, seguimiento de envíos, gestión de flotas, servicio al cliente) dentro del contexto general?

*(El diagrama de contexto se encuentra en `diagramas/contexto.mmd` y debe completarse con los actores y relaciones identificados en el Event Storming.)*

---

### 2. Vista de Contenedores
> Preguntas guía:
> - ¿Qué contenedores (servicios, bases de datos, colas, APIs) componen la plataforma y cuál es su responsabilidad principal?
> - ¿Cómo se comunican los contenedores entre sí (sincrónico vs. asíncrono, protocolos, formatos de datos)?
> - ¿Qué tecnologías se seleccionan para cada contenedor y qué trade-offs implican (ej: escalabilidad vs. consistencia, latencia vs. costo)?
> - ¿Dónde se implementan los patrones de integración (event-driven, CQRS, saga, outbox) y cómo afectan a los atributos de calidad?

*(Completar con un diagrama C4 de contenedores que muestre los límites técnicos y las dependencias entre ellos.)*

---

### 3. Vista de Componentes
> Preguntas guía:
> - Para cada contenedor, ¿qué componentes internos lo componen y cuál es su responsabilidad?
> - ¿Cómo se modularizan los componentes dentro de cada contexto (ej: gestión de pedidos: `OrderCommandHandler`, `OrderQueryService`, `OrderEventPublisher`)?
> - ¿Qué contratos definen las fronteras entre componentes (interfaces, APIs, eventos, DTOs) y cómo se versionan?
> - ¿Qué tácticas arquitectónicas se aplican para cumplir con los ASRs (ej: caché distribuido para rendimiento, circuit breaker para resiliencia)?

*(Completar con diagramas C4 de componentes para los contenedores críticos, detallando los contratos en cada frontera.)*

---

### 4. Vista de Despliegue
> Preguntas guía:
> - ¿En qué infraestructura se despliega la plataforma (nube, on-premise, híbrida) y qué servicios gestionados se utilizan (ej: AWS Lambda, EKS, RDS)?
> - ¿Cómo se escala horizontal y verticalmente cada contenedor para cumplir con los ASRs de rendimiento y disponibilidad?
> - ¿Qué estrategias de despliegue se implementan (blue-green, canary, feature flags) y cómo mitigan riesgos?
> - ¿Cómo se monitorizan y observan los componentes en producción para detectar cuellos de botella o fallos?

*(Completar con un diagrama C4 de despliegue que muestre la topología de infraestructura y las dependencias de servicios externos.)*

---

### 5. Decisiones Arquitectónicas Clave
> Preguntas guía:
> - ¿Qué decisiones de diseño se tomaron en las iteraciones de ADD 3.0 y cómo impactan en los atributos de calidad?
> - ¿Qué patrones de integración se seleccionaron (ej: event sourcing, CQRS, saga) y por qué?
> - ¿Cómo se gestionan los datos distribuidos (consistencia eventual vs. fuerte, particionamiento, replicación)?
> - ¿Qué riesgos arquitectónicos se identificaron en el ATAM y qué mitigaciones se propusieron?

*(Referenciar los ADRs en la carpeta `adr/` que documentan estas decisiones.)*

---

## Límites y Contratos

| Frontera                     | Tipo de Contrato               | Ejemplo de Contrato (a definir)                     |
|------------------------------|---------------------------------|------------------------------------------------------|
| API Gateway ↔ Gestión Pedidos| API REST (OpenAPI)             | `POST /pedidos` con schema `Pedido` y headers JWT    |
| Gestión Pedidos ↔ Seguimiento| Eventos asíncronos (AsyncAPI)  | `EnvioCreado` con payload `envio_id` y `estado`      |
| Seguimiento ↔ Gestión Flotas | API GraphQL                    | `query { flota(disponible: true) { id, ubicacion } }`|
| Servicio Cliente ↔ CRM       | API SOAP                       | `GetClienteRequest` con XML schema definido          |

> **Nota:** Los contratos deben definirse con precisión en los diagramas C4 y en los archivos de especificación (OpenAPI/AsyncAPI).

---

## Tácticas Arquitectónicas por Atributo de Calidad

| Atributo de Calidad | Táctica Seleccionada               | Implementación Propuesta                          |
|---------------------|-------------------------------------|----------------------------------------------------|
| Rendimiento         | Caché distribuido                  | Redis con TTL de 5 min para consultas frecuentes    |
| Escalabilidad       | Particionamiento horizontal         | Sharding por región geográfica en base de datos    |
| Disponibilidad      | Circuit Breaker + Retry             | Resilience4j con fallback a caché local            |
| Seguridad           | Zero Trust                         | Autenticación JWT + RBAC + mTLS interno            |
| Mantenibilidad      | Modularización por contexto DDD     | Módulos independientes con contratos explícitos    |

> Preguntas guía:
> - ¿Qué otras tácticas se evaluaron para cada atributo y por qué se descartaron?
> - ¿Cómo se validará la efectividad de cada táctica (métricas, pruebas de carga, pentesting)?

---

## Sistema Actual (As-Is)

### Descripción del Sistema Legado
- **Arquitectura:** Monolítica con base de datos SQL centralizada (PostgreSQL) y APIs REST expuestas a clientes internos.
- **Problemas Identificados:**
  - **Acoplamiento alto:** Todos los módulos dependen de la misma base de datos y comparten lógica de negocio.
  - **Escalabilidad limitada:** La base de datos se convierte en cuello de botella bajo carga (máximo 1,000 TPS).
  - **Falta de resiliencia:** Las caídas del servicio central afectan a todas las funcionalidades.
  - **Tiempo de despliegue:** Los releases tardan 2 horas por pruebas manuales y dependencias entre módulos.
- **Integraciones:**
  - **CRM:** API SOAP con tiempo de respuesta > 500ms en p95.
  - **Flota de camiones:** Sistema propietario con latencia de 2s para actualizar ubicaciones.
  - **Pagos:** Servicio externo con tasa de fallos del 2% en transacciones.

> Preguntas guía:
> - ¿Qué componentes del sistema actual se pueden reutilizar y cuáles deben reemplazarse?
> - ¿Cómo se migra la base de datos sin downtime y manteniendo la consistencia?
> - ¿Qué estrategias de convivencia (strangler pattern, sidecar) se implementan durante la migración?

---

## Estrategia de Migración

### Fases de Migración
1. **Fase 1: Establecer Límites de Contexto**
   - Identificar contextos DDD y definir contratos entre ellos.
   - Implementar un API Gateway para enrutar peticiones al sistema legado o a los nuevos servicios.

2. **Fase 2: Desacoplar Módulos Críticos**
   - Extraer el módulo de **Gestión de Pedidos** como microservicio independiente.
   - Implementar un patrón **Outbox** para sincronizar eventos con el sistema legado.

3. **Fase 3: Migrar Datos y Eventos**
   - Usar **Change Data Capture (CDC)** para replicar datos a la nueva base de datos.
   - Implementar un **Saga Pattern** para coordinar transacciones distribuidas.

4. **Fase 4: Optimizar y Escalar**
   - Aplicar tácticas de rendimiento (caché, particionamiento) y resiliencia (circuit breaker).
   - Realizar pruebas de carga para validar los ASRs.

> Preguntas guía:
> - ¿Qué métricas se monitorean durante cada fase para asegurar el éxito de la migración?
> - ¿Cómo se maneja la consistencia de datos entre el sistema legado y los nuevos servicios?
> - ¿Qué herramientas se utilizan para orquestar la migración (ej: Kubernetes, Terraform, Debezium)?

---

## Herramientas y Tecnologías Propuestas

| Categoría               | Herramientas Seleccionadas (a evaluar)                          |
|------------------------|------------------------------------------------------------------|
| Lenguajes              | Python (FastAPI), Java (Spring Boot), Go (para servicios críticos) |
| Frameworks             | FastAPI (API Gateway), Spring Boot (microservicios), React (frontend) |
| Base de Datos          | PostgreSQL (OLTP), DynamoDB (eventos), Redis (caché)             |
| Mensajería             | Kafka (eventos), RabbitMQ (colas de trabajo)                     |
| Orquestación           | Kubernetes (EKS), Docker Swarm                                   |
| Observabilidad         | Prometheus + Grafana, OpenTelemetry, ELK Stack                   |
| Seguridad              | Keycloak (IAM), Vault (secretos), mTLS (comunicación interna)    |
| CI/CD                  | GitHub Actions, ArgoCD (GitOps), Jenkins                         |

> Preguntas guía:
> - ¿Qué criterios se usaron para seleccionar estas herramientas y qué alternativas se descartaron?
> - ¿Cómo se garantiza la interoperabilidad entre tecnologías (ej: Kafka ↔ PostgreSQL CDC)?
> - ¿Qué costos operativos y de licencias implica esta selección?

---

## Riesgos Arquitectónicos (a documentar en `riesgos-y-mitigaciones.md`)

| Riesgo                              | Impacto Potencial                     | Probabilidad |
|-------------------------------------|----------------------------------------|--------------|
| Inconsistencia de datos en migración| Pérdida de pedidos o duplicación       | Alta         |
| Latencia en integraciones externas  | Degradación del rendimiento (p99 > 1s) | Media        |
| Fallos en la coordinación de sagas  | Transacciones bloqueadas               | Media        |
| Sobrecarga de la base de datos      | Caída del servicio bajo carga          | Alta         |
| Vulnerabilidades de seguridad       | Exposición de datos sensibles          | Baja         |

> **Nota:** Priorizar los riesgos en `riesgos-y-mitigaciones.md` usando la matriz de impacto/probabilidad.

---

## Próximos Pasos
1. Completar el diagrama de contexto (`diagramas/contexto.mmd`) con los actores y relaciones del Event Storming.
2. Definir los escenarios de calidad en `atributos-de-calidad.md` con métricas y umbrales.
3. Escribir los ADRs para las decisiones clave (ej: `adr/002-diseno-arquitectonico.md`).
4. Diseñar los diagramas C4 de contenedores y componentes para los contextos críticos.
5. Realizar la evaluación ATAM y documentar los riesgos en `riesgos-y-mitigaciones.md`.

---

*Este documento es un marco de trabajo. Las secciones en blanco deben completarse con el análisis y decisiones del candidato.*

// === ARCHIVO: README.md ===
# Plataforma Logística: Diseño y Evaluación de Arquitectura

## Contexto del Negocio

**Empresa:** LogiTech Solutions (proveedor de soluciones logísticas para e-commerce y retail).

**Problema:**
La plataforma logística actual es un monolito con más de 5 años de antigüedad que no escala para soportar el crecimiento del negocio. En los últimos 6 meses, se han registrado:
- **Aumento del 300% en volumen de pedidos** (de 5,000 a 20,000 pedidos/día).
- **Degradación del rendimiento:** El tiempo de respuesta del endpoint de creación de pedidos supera los 2s en p95.
- **Fallas frecuentes:** 12 incidentes críticos en el último trimestre por sobrecarga de la base de datos.
- **Incapacidad para innovar:** Los releases toman 2 semanas por pruebas manuales y dependencias entre módulos.

**Objetivo:**
Rediseñar la arquitectura para soportar 50,000 pedidos/día con un p99 < 80ms, garantizar un 99.95% de disponibilidad y reducir el tiempo de despliegue a menos de 1 hora.

---

## Actores y Sistemas Externos

### Actores
1. **Cliente Final:**
   - Realiza pedidos a través de la app móvil o web.
   - Consulta el estado de sus envíos.
   - Cancela pedidos antes de que sean despachados.

2. **Operador Logístico:**
   - Gestiona la flota de camiones y conductores.
   - Actualiza el estado de los envíos (en tránsito, entregado, fallido).

3. **Soporte al Cliente:**
   - Resuelve incidencias reportadas por clientes.
   - Accede al historial de pedidos y envíos.

4. **Equipo de Finanzas:**
   - Genera reportes de ingresos y costos por región.
   - Valida las transacciones de pago.

### Sistemas Externos
1. **CRM (Salesforce):**
   - Proporciona datos de clientes (nombre, dirección, historial de compras).
   - Latencia: ~500ms en p95.
   - Protocolo: SOAP.

2. **Sistema de Flota (Propietario):**
   - Gestiona la disponibilidad y ubicación de camiones.
   - Latencia: ~2s para actualizar ubicaciones.
   - Protocolo: API REST con autenticación básica.

3. **Procesador de Pagos (Stripe):**
   - Valida y procesa pagos con tarjeta.
   - Tasa de fallos: 2% en transacciones.
   - Protocolo: API REST con webhooks.

4. **Servicio de Mapas (Google Maps API):**
   - Calcula rutas óptimas para los envíos.
   - Costo: $0.50 por 1,000 llamadas.
   - Latencia: ~300ms en p90.

---

## Atributos de Calidad (ASRs)

| ASR                          | Valor Medible                          | Métrica de Éxito                          |
|------------------------------|----------------------------------------|--------------------------------------------|
| Escalabilidad                | 50,000 pedidos/día                     | Throughput de 500 TPS en p99              |
| Rendimiento                  | Tiempo de respuesta de creación de pedido | p99 < 80ms para `POST /pedidos`          |
| Disponibilidad               | 99.95%                                 | Máximo 21.9 minutos de downtime/mes      |
| Consistencia de Datos        | Cero pedidos duplicados o perdidos     | Tasa de error < 0.01% en transacciones   |
| Seguridad                    | Cumplimiento con PCI DSS y GDPR        | 0 vulnerabilidades críticas en pentest    |
| Mantenibilidad               | Tiempo de despliegue < 1 hora          | Pipeline CI/CD con rollback en < 5 min   |

---

## Restricciones

1. **Tecnológicas:**
   - El sistema de flota (propietario) **no puede modificarse** en los próximos 12 meses.
   - La base de datos PostgreSQL actual **debe migrarse sin downtime**.
   - El frontend (React) **debe mantener la misma interfaz** durante la migración.

2. **Regulatorias:**
   - Los datos de clientes deben almacenarse en servidores dentro de la UE (GDPR).
   - Las transacciones de pago deben cumplir con PCI DSS.

3. **Presupuestarias:**
   - El costo operativo mensual **no debe superar los $50,000 USD**.
   - Se dispone de un equipo de 5 desarrolladores full-time para la migración.

4. **Temporales:**
   - La migración debe completarse en **6 meses**.
   - Cada fase de migración debe entregarse en sprints de 2 semanas.

---

## Dominios Principales

1. **Gestión de Pedidos:**
   - Creación, validación y procesamiento de pedidos.
   - Integración con CRM y procesador de pagos.

2. **Seguimiento de Envíos:**
   - Actualización del estado de envíos en tiempo real.
   - Notificaciones a clientes (email/SMS).

3. **Gestión de Flotas:**
   - Asignación de camiones y conductores a envíos.
   - Optimización de rutas con Google Maps API.

4. **Servicio al Cliente:**
   - Gestión de incidencias y devoluciones.
   - Acceso al historial de pedidos y envíos.

5. **Reportes y Analítica:**
   - Generación de reportes de rendimiento logístico.
   - Análisis de costos y rutas óptimas.

---

## Estructura del Proyecto

```
logistics-platform/
├── adr/                     # Architecture Decision Records (ADRs)
│   ├── 001-contexto-logistico.md
│   └── 002-diseno-arquitectonico.md
├── diagramas/               # Diagramas C4 en Mermaid/PlantUML
│   └── contexto.mmd
├── docs/                    # Documentación adicional
│   └── setup.md             # Guía de instalación y ejecución
├── poc/                     # Proof of Concept (opcional, máximo 3 archivos)
│   ├── api-gateway-service/
│   │   └── main.py           # Ejemplo de API Gateway con FastAPI
│   ├── docker-compose.yml   # Entorno local para pruebas
│   └── README.md            # Instrucciones del PoC
├── atributos-de-calidad.md  # Escenarios de calidad con métricas
├── arquitectura.md          # Vistas de arquitectura (contexto, contenedores, componentes, despliegue)
├── README.md                # Este archivo (caso de negocio y guía)
├── riesgos-y-mitigaciones.md# Matriz de riesgos priorizados
└── rubrica-autoevaluacion.md# Rubrica de evaluación
```

---

## Entregables Esperados

1. **Mapa de Eventos y Procesos Logísticos** (Resultado del Event Storming).
2. **Mapa de Contextos DDD** (Límites y responsabilidades de cada contexto).
3. **Documento de Diseño Iterativo** (Aplicación de ADD 3.0 con decisiones arquitectónicas).
4. **Informe de Evaluación ATAM** (Riesgos de rendimiento, escalabilidad y mitigaciones).
5. **Diagramas C4** (Contexto, contenedores, componentes y despliegue).
6. **ADRs** (Decisiones clave con contexto, fuerzas, opciones y consecuencias).
7. **Matriz de Riesgos** (Priorizados por impacto y probabilidad).

---

## Guía de Entrega

1. **Fase 1: Event Storming**
   - Facilitar una sesión con stakeholders para identificar eventos clave del dominio.
   - Documentar los eventos en el formato: `Evento: [Nombre] - Descripción: [Qué ocurre] - Actores: [Quién lo desencadena]`.
   - Ejemplo:
     ```
     Evento: PedidoCreado
     Descripción: Un cliente realiza un pedido a través de la app/web.
     Actores: Cliente Final
     ```

2. **Fase 2: Mapa de Contextos DDD**
   - Definir los contextos delimitados (ej: Gestión de Pedidos, Seguimiento de Envíos).
   - Establecer los contratos entre contextos (APIs, eventos, DTOs).
   - Documentar las responsabilidades de cada contexto en `arquitectura.md`.

3. **Fase 3: Iteraciones de Diseño con ADD 3.0**
   - Para cada atributo de calidad (ASR), seleccionar tácticas arquitectónicas.
   - Documentar las decisiones en ADRs (ej: `adr/002-diseno-arquitectonico.md`).
   - Diseñar los diagramas C4 de contenedores y componentes.

4. **Fase 4: Evaluación ATAM**
   - Identificar riesgos de rendimiento y escalabilidad.
   - Priorizarlos en `riesgos-y-mitigaciones.md` usando la matriz de impacto/probabilidad.
   - Proponer mitigaciones para los riesgos críticos.

---

## Cómo Empezar

1. **Clonar el repositorio** (o descargar el ZIP generado por el asistente de IA):
   ```bash
   git clone <repositorio>
   cd logistics-platform
   ```

2. **Completar el diagrama de contexto** (`diagramas/contexto.mmd`):
   - Usar Mermaid o PlantUML para dibujar los actores y sistemas externos.
   - Ejemplo de sintaxis Mermaid:
     ```mermaid
     C4Context
       title Contexto de la Plataforma Logística
       Person(cliente, "Cliente Final", "Realiza pedidos y consulta envíos")
       System(crm, "CRM (Salesforce)", "Proporciona datos de clientes")
       System_Ext(flota, "Sistema de Flota", "Gestiona camiones y conductores")
       Rel(cliente, flota, "Consulta estado de envío")
       Rel(crm, flota, "Proporciona datos de clientes", "SOAP")
     ```

3. **Definir escenarios de calidad** (`atributos-de-calidad.md`):
   - Completar la tabla con fuente, estímulo, artefacto, entorno, respuesta y medida.

4. **Escribir los ADRs** (`adr/`):
   - Usar la plantilla estricta (solo contexto y fuerzas van escritas).

5. **Diseñar los diagramas C4** para contenedores y componentes.

6. **Realizar la evaluación ATAM** y documentar riesgos en `riesgos-y-mitigaciones.md`.

---

## Evaluación

El candidato será evaluado según los siguientes criterios (detallados en `rubrica-autoevaluacion.md`):
1. **Alineación con los ASRs:** ¿Las decisiones arquitectónicas cumplen con los atributos de calidad?
2. **Uso de patrones y herramientas:** ¿Se aplican patrones de integración (event-driven, saga, outbox) y herramientas adecuadas?
3. **Calidad de diagramas y ADRs:** ¿Los diagramas C4 y ADRs son claros, completos y siguen las convenciones?
4. **Viabilidad técnica:** ¿La arquitectura propuesta es viable con las restricciones tecnológicas y presupuestarias?

---

## Recursos Adicionales

- [Documentación de C4 Model](https://c4model.com/)
- [Plantilla de ADR](https://github.com/joelparkerhenderson/architecture-decision-record)
- [ADD 3.0 (Attribute-Driven Design)](https://www.sei.cmu.edu/our-work/projects/display.cfm?customel_datapageid_4050=6168)
- [ATAM (Architecture Tradeoff Analysis Method)](https://www.sei.cmu.edu/our-work/projects/display.cfm?customel_datapageid_4050=6166)
- [Mermaid Live Editor](https://mermaid.live/)
- [PlantUML Web Server](http://www.plantuml.com/plantuml/)

---

*Este repositorio contiene el caso de negocio y las plantillas para el reto. El candidato debe completar los artefactos con sus análisis y decisiones.*

// === ARCHIVO: atributos-de-calidad.md ===
# Atributos de Calidad y Escenarios

## Atributos de Calidad (ASRs)

| ASR               | Descripción                                                                 | Métrica de Éxito                          |
|--------------------|-----------------------------------------------------------------------------|--------------------------------------------|
| Escalabilidad      | Capacidad para manejar un aumento en el volumen de pedidos sin degradación. | Throughput de 500 TPS en p99              |
| Rendimiento        | Tiempo de respuesta rápido para operaciones críticas.                      | p99 < 80ms para `POST /pedidos`          |
| Disponibilidad     | El sistema debe estar disponible el 99.95% del tiempo.                     | Máximo 21.9 minutos de downtime/mes      |
| Consistencia       | Garantizar que los pedidos no se pierdan ni dupliquen.                     | Tasa de error < 0.01% en transacciones   |
| Seguridad          | Protección de datos sensibles y cumplimiento normativo.                    | 0 vulnerabilidades críticas en pentest    |
| Mantenibilidad     | Facilidad para realizar cambios y desplegar nuevas versiones.               | Tiempo de despliegue < 1 hora            |

---

## Escenarios de Calidad

Cada escenario sigue el formato:
- **Fuente:** Actor o sistema que genera el estímulo.
- **Estímulo:** Evento o acción que afecta al sistema.
- **Artefacto:** Parte del sistema afectada.
- **Entorno:** Condiciones bajo las cuales ocurre el estímulo.
- **Respuesta:** Comportamiento del sistema ante el estímulo.
- **Medida:** Métrica para evaluar el éxito de la respuesta.

Completar la tabla con los escenarios para cada ASR:

| ASR               | Fuente               | Estímulo                                      | Artefacto                     | Entorno               | Respuesta                                      | Medida                              |
|--------------------|----------------------|------------------------------------------------|-------------------------------------|-----------------------|------------------------------------------------|--------------------------------------|
| Escalabilidad      | Cliente Final        | Pico de 10,000 pedidos en 5 minutos            | API de Creación de Pedidos          | Producción            | El sistema procesa todos los pedidos           | Throughput ≥ 500 TPS                |
|                    |                      |                                                |                                     |                       | sin degradación de rendimiento.                | p99 < 80ms                          |
| Rendimiento        | Operador Logístico   | Consulta masiva de estados de envío (1,000 RPM)| Servicio de Seguimiento de Envíos   | Producción            | El sistema responde en menos de 100ms.         | p99 < 100ms                         |
| Disponibilidad     | Sistema de Pagos     | Falla en el servicio de pagos (Stripe)         | Servicio de Procesamiento de Pagos  | Producción            | El sistema usa un fallback y notifica al equipo.| Tiempo de recuperación < 2 min      |
| Consistencia       | Cliente Final        | Pedido duplicado por error en el frontend      | Servicio de Gestión de Pedidos      | Producción            | El sistema detecta y elimina el duplicado.     | 0 pedidos duplicados                |
| Seguridad          | Hacker               | Intento de inyección SQL en el endpoint de login| API Gateway                        | Producción            | El sistema bloquea la petición y registra el evento. | 0 accesos no autorizados       |
| Mantenibilidad     | Desarrollador        | Cambio en la lógica de asignación de flotas    | Servicio de Gestión de Flotas       | Desarrollo            | El cambio se implementa y despliega en < 1 hora. | Tiempo de despliegue < 1 hora    |

---

## Escenarios Adicionales (a definir)

> Preguntas guía:
> - ¿Qué otros escenarios críticos no están cubiertos en la tabla anterior?
> - Para cada escenario, ¿qué tácticas arquitectónicas se aplican para cumplir con la medida de éxito?
> - ¿Cómo se validan estos escenarios (pruebas de carga, pentesting, simulación)?

*(Agregar filas adicionales según sea necesario.)*

---

## Métricas y Umbrales

| Métrica                     | Umbral de Éxito       | Herramienta de Medición               |
|-----------------------------|------------------------|----------------------------------------|
| Throughput (TPS)            | ≥ 500                  | Prometheus + Grafana                   |
| Tiempo de Respuesta (p99)   | < 80ms                 | OpenTelemetry + Jaeger                 |
| Disponibilidad              | ≥ 99.95%               | Prometheus + AlertManager              |
| Tasa de Error               | < 0.01%                | ELK Stack                              |
| Tiempo de Despliegue        | < 1 hora               | GitHub Actions / ArgoCD                |

---

## Tácticas Arquitectónicas por Escenario

| Escenario                   | Táctica Seleccionada               | Justificación                                                                 |
|-----------------------------|-------------------------------------|---------------------------------------------------------------------------------|
| Pico de pedidos             | Particionamiento horizontal         | Distribuye la carga entre múltiples instancias del servicio de pedidos.        |
| Consulta masiva de envíos   | Caché distribuido (Redis)          | Reduce la carga en la base de datos y mejora el tiempo de respuesta.           |
| Falla en servicio de pagos  | Circuit Breaker + Fallback          | Aísla el fallo y usa un proveedor alternativo o modo degradado.                |
| Pedido duplicado            | Idempotencia en API                 | Garantiza que un mismo pedido no se procese más de una vez.                   |
| Inyección SQL               | WAF + Validación de inputs          | Bloquea peticiones maliciosas y sanitiza entradas.                            |
| Cambio en lógica de flotas  | Modularización + Feature Flags      | Permite desplegar cambios sin afectar otras funcionalidades.                  |

> Preguntas guía:
> - ¿Qué otras tácticas se evaluaron para cada escenario y por qué se descartaron?
> - ¿Cómo se implementan estas tácticas en la arquitectura (herramientas, patrones)?
> - ¿Qué riesgos introduce cada táctica y cómo se mitigan?

---

## Validación de Escenarios

> Preguntas guía:
> - ¿Qué pruebas se diseñan para validar cada escenario (ej: pruebas de carga para escalabilidad, pentesting para seguridad)?
> - ¿Qué herramientas se utilizan para generar la carga o simular fallos?
> - ¿Cómo se monitorean los umbrales durante las pruebas?

*(Completar con un plan de validación para cada escenario.)*

---

*Este documento proporciona el marco para definir los escenarios de calidad. Las filas en blanco deben completarse con el análisis del candidato.*"


// === ARCHIVO: riesgos-y-mitigaciones.md ===
# Matriz de Riesgos y Mitigaciones

## Contexto
La plataforma logística debe soportar la operación de más de 50,000 pedidos diarios con un tiempo de procesamiento promedio inferior a 2 segundos por pedido. Además, debe garantizar la sincronización en tiempo real entre los sistemas de inventario, transporte y atención al cliente, operando en una infraestructura multi-región con tolerancia a fallos.

La arquitectura propuesta debe manejar picos de demanda durante eventos comerciales (ej: Black Friday) donde el volumen de pedidos puede triplicarse, manteniendo la consistencia de datos y la disponibilidad del servicio. Los sistemas externos involucrados (ERP, WMS, TMS) tienen limitaciones de throughput y latencia conocidas, lo que introduce riesgos en la integración.

## Matriz de Riesgos

| Riesgo                                                                 | Probabilidad (Alta/Media/Baja) | Impacto (Alto/Medio/Bajo) | Tratamiento                                                                                     |
|-----------------------------------------------------------------------|-------------------------------|--------------------------|-------------------------------------------------------------------------------------------------|
|                                                                       |                               |                          |                                                                                                 |
| **Rendimiento degradado bajo carga alta**                            | Alta                           | Alto                     |                                                                                                 |
| *Los servicios de orquestación no escalan horizontalmente, causando colas de pedidos.* |                               |                          |                                                                                                 |

| **Inconsistencia de datos entre contextos**                          | Media                          | Alto                     |                                                                                                 |
| *Fallas en la sincronización entre inventario y transporte generan pedidos con stock no disponible.* |                               |                          |                                                                                                 |

| **Latencia en integración con sistemas externos (ERP/WMS/TMS)**     | Alta                           | Medio                    |                                                                                                 |
| *Los sistemas legados no soportan más de 100 TPS, limitando el throughput del sistema.* |                               |                          |                                                                                                 |

| **Falta de visibilidad en tiempo real de la cadena logística**      | Baja                           | Alto                     |                                                                                                 |
| *Los eventos de dominio no se propagan con la suficiente velocidad para actualizar dashboards.* |                               |                          |                                                                                                 |

| **Fallos en la tolerancia a fallos regional**                        | Media                          | Alto                     |                                                                                                 |
| *La caída de una región deja sin servicio a un porcentaje de usuarios hasta que el failover se complete.* |                               |                          |                                                                                                 |

| **Complejidad excesiva en la orquestación de procesos**             | Alta                           | Medio                    |                                                                                                 |
| *El flujo de pedidos involucra múltiples pasos asíncronos, aumentando la probabilidad de errores.* |                               |                          |                                                                                                 |

| **Dependencia crítica de servicios externos**                        | Media                          | Alto                     |                                                                                                 |
| *La indisponibilidad de un proveedor de transporte (ej: FedEx API) bloquea la creación de envíos.* |                               |                          |                                                                                                 |

| **Falta de estandarización en contratos de API**                     | Baja                           | Medio                    |                                                                                                 |
| *Los equipos trabajan con versiones distintas de los esquemas de datos, generando errores de serialización.* |                               |                          |                                                                                                 |

| **Sobrecarga en la base de datos de reporting**                      | Media                          | Bajo                     |                                                                                                 |
| *Las consultas analíticas afectan el rendimiento de las transacciones operativas.*              |                               |                          |                                                                                                 |

| **Seguridad insuficiente en la comunicación entre servicios**       | Baja                           | Alto                     |                                                                                                 |
| *Datos sensibles (direcciones, pagos) viajan sin cifrado entre contextos.*                     |                               |                          |                                                                                                 |

## Preguntas Guía para Completar la Matriz
1. **¿Qué riesgos adicionales identificas** en el contexto descrito? Considera aspectos como:
   - Escalabilidad de los servicios de orquestación.
   - Consistencia eventual vs. fuerte en transacciones distribuidas.
   - Latencia en la propagación de eventos.
   - Dependencias ocultas entre contextos.

2. **Para cada riesgo, define métricas cuantificables** que permitan medir su probabilidad e impacto. Ejemplos:
   - Probabilidad: "% de pedidos que superan 2 segundos de procesamiento durante picos de carga".
   - Impacto: "Número de pedidos rechazados por stock no disponible en las últimas 24 horas".

3. **¿Qué estrategias de mitigación propondrías** para los riesgos identificados? Considera:
   - Patrones de diseño (ej: Saga, Outbox, Circuit Breaker).
   - Herramientas de monitoreo y observabilidad.
   - Estrategias de despliegue (ej: canary releases, blue-green).
   - Mecanismos de recuperación (ej: retries con backoff exponencial, compensaciones).

4. **Prioriza los riesgos** utilizando una matriz de impacto/probabilidad. ¿Cuáles son los 3 riesgos más críticos que requieren atención inmediata?

5. **¿Cómo validarías la efectividad** de las estrategias de mitigación? Propón pruebas o métricas para cada una.

---

// === ARCHIVO: rubrica-autoevaluacion.md ===
# Rúbrica de Autoevaluación

## Criterios de Evaluación

### 1. Alineación con los Requisitos Arquitectónicamente Significativos (ASRs)

| Nivel          | Descripción                                                                                                                                                                                                 | Puntuación |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| **Excelente** | Los diseños y decisiones arquitectónicas **demuestran una alineación clara y cuantificable** con todos los ASRs definidos en el caso (ej: escalabilidad a 50,000 pedidos/día, latencia p99 < 2s). Se incluyen métricas específicas para validar el cumplimiento. | 5          |
| **Aceptable** | Los diseños abordan los ASRs, pero **falta precisión en las métricas** o no se justifica cómo cada decisión contribuye a cumplirlos. Algunos ASRs quedan sin respuesta clara.                                              | 3          |
| **Insuficiente** | Los diseños **no están alineados** con los ASRs o los abordan de manera superficial. Las decisiones arquitectónicas no consideran los umbrales definidos (ej: no se menciona cómo se maneja la carga pico).                     | 1          |

### 2. Uso de Patrones y Herramientas Arquitectónicas

| Nivel          | Descripción                                                                                                                                                                                                 | Puntuación |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| **Excelente** | **Aplica correctamente** patrones arquitectónicos (ej: CQRS, Event Sourcing, Sagas) y herramientas (ej: Kafka para eventos, Redis para caché) **justificando su elección** con criterios técnicos y de negocio. Se detallan las ventajas y trade-offs de cada patrón. | 5          |
| **Aceptable** | Usa patrones y herramientas, pero **no justifica su elección** o mezcla patrones incompatibles (ej: Event Sourcing con consistencia fuerte). Algunos patrones se aplican de manera superficial.                                      | 3          |
| **Insuficiente** | **No aplica patrones arquitectónicos relevantes** o los usa de manera incorrecta. Las herramientas seleccionadas no resuelven los problemas descritos en el caso.                                                    | 1          |

### 3. Calidad de los Diagramas y Documentación

| Nivel          | Descripción                                                                                                                                                                                                 | Puntuación |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| **Excelente** | Los diagramas (C4, secuencia, estados) **son claros, completos y siguen estándares** (ej: Mermaid, PlantUML). Incluyen contratos explícitos en las fronteras entre componentes y actores. La documentación es precisa y autoexplicativa. | 5          |
| **Aceptable** | Los diagramas son comprensibles, pero **les falta detalle** (ej: no se especifican contratos en las fronteras) o no siguen estándares. La documentación es genérica y no profundiza en aspectos críticos.                              | 3          |
| **Insuficiente** | Los diagramas **son confusos, incompletos o no reflejan el diseño propuesto**. La documentación es vaga o contiene errores conceptuales.                                                                   | 1          |

### 4. Calidad de los ADRs (Architecture Decision Records)

| Nivel          | Descripción                                                                                                                                                                                                 | Puntuación |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| **Excelente** | Los ADRs **siguen la plantilla estricta** (contexto, fuerzas, opciones, decisión, consecuencias) y **analizan al menos 3 alternativas** para cada decisión. Las opciones se evalúan con criterios técnicos y de negocio medibles. | 5          |
| **Aceptable** | Los ADRs cumplen con la estructura, pero **el análisis de opciones es superficial** (ej: solo 1 o 2 alternativas) o no incluye métricas. Algunas decisiones no están bien justificadas.                              | 3          |
| **Insuficiente** | Los ADRs **no siguen la plantilla** o están incompletos. Las decisiones se toman sin análisis previo de alternativas o sin considerar consecuencias.                                                     | 1          |

### 5. Viabilidad y Complejidad Técnica

| Nivel          | Descripción                                                                                                                                                                                                 | Puntuación |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| **Excelente** | La solución propuesta **es viable técnicamente** y considera restricciones reales (ej: latencia de APIs externas, throughput de bases de datos). Se incluyen pruebas de concepto o cálculos que validan la escalabilidad y el rendimiento. | 5          |
| **Aceptable** | La solución es viable, pero **no se profundiza en cómo se superarían las restricciones técnicas**. Falta evidencia (ej: cálculos, simulaciones) que respalde la escalabilidad.                                  | 3          |
| **Insuficiente** | La solución **no es viable técnicamente** o ignora restricciones críticas del caso. No hay análisis de factibilidad o los cálculos son incorrectos.                                                        | 1          |

## Instrucciones para la Autoevaluación
1. **Evalúa cada criterio** utilizando la descripción de los niveles (Excelente, Aceptable, Insuficiente).
2. **Asigna una puntuación** (5, 3 o 1) a tu trabajo en cada criterio.
3. **Justifica brevemente** por qué asignaste esa puntuación, mencionando:
   - **Qué hiciste bien** en relación con el criterio.
   - **Qué aspectos podrían mejorarse** y cómo.
4. **Prioriza las mejoras**: identifica los 2 criterios con menor puntuación y define acciones concretas para elevarlos.

## Ejemplo de Autoevaluación

| Criterio                                      | Nivel Asignado | Justificación                                                                                                                                                                                                 | Acciones de Mejora                                                                                     |
|-----------------------------------------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| 1. Alineación con los ASRs                    | Aceptable        | Los diseños consideran los ASRs, pero no se incluyen métricas específicas para validar la latencia p99 < 2s.                                                                                             | Incluir cálculos de throughput y latencia en el documento de arquitectura.                          |
| 2. Uso de Patrones y Herramientas             | Excelente        | Se aplicó el patrón Saga para manejar la consistencia eventual y Kafka para eventos, justificando su elección con trade-offs claros.                                                                     | Ninguna.                                                                                             |

## Preguntas Guía para la Reflexión
1. **¿Lograste identificar trade-offs claros** en tus decisiones arquitectónicas? ¿Cómo los documentaste?
2. **¿Tus diagramas comunican efectivamente** la arquitectura a un equipo técnico y no técnico? ¿Qué mejoras harías?
3. **¿Los ADRs son lo suficientemente detallados** para que otro arquitecto entienda las decisiones tomadas? ¿Qué información adicional incluirías?
4. **¿La solución propuesta es escalable** para manejar el crecimiento futuro del negocio? ¿Qué ajustes harías para soportar un aumento del 50% en el volumen de pedidos?
5. **¿Consideraste todos los actores del sistema** (usuarios, sistemas externos, equipos de operaciones) en tu diseño? ¿Qué actores faltan y cómo los integrarías?

// === ARCHIVO: adr/001-contexto-logistico.md ===
# ADR 001: Contexto Logístico de la Plataforma

Estado: Propuesto
Fecha: 2025-MM-DD

## Contexto

La plataforma logística debe gestionar la recepción, procesamiento y entrega de pedidos para una cadena de suministro global. Actualmente, el sistema enfrenta los siguientes desafíos:

- **Volumen de pedidos**: 50.000 pedidos diarios con picos de hasta 100.000 en temporadas altas.
- **Actores involucrados**: Clientes finales, proveedores, transportistas, centros de distribución y sistemas de inventario.
- **Sistemas externos**: ERP (SAP), sistema de gestión de transportes (TMS), pasarela de pagos (Stripe) y servicio de geolocalización (Google Maps API).
- **Requisitos no funcionales**: 
  - **Rendimiento**: Tiempo de procesamiento de un pedido < 2 segundos (p99).
  - **Escalabilidad**: Capacidad para manejar un crecimiento del 20% anual en volumen.
  - **Disponibilidad**: 99.95% de uptime.
  - **Consistencia**: Datos de inventario y estado de pedidos sincronizados en tiempo real.

La plataforma actual opera como un monolito con integraciones punto a punto, lo que genera acoplamiento alto y dificultad para escalar componentes individuales.

## Fuerzas

- **Tensión entre rendimiento y consistencia**: La sincronización en tiempo real de inventario y pedidos requiere transacciones distribuidas, lo que puede impactar el rendimiento.
- **Variabilidad en tiempos de entrega**: Dependencia de múltiples transportistas con diferentes SLAs y APIs.
- **Gestión de fallos**: Necesidad de manejar fallos en sistemas externos (ej: TMS no disponible) sin bloquear el procesamiento de pedidos.
- **Regulaciones**: Cumplimiento de normativas locales e internacionales (GDPR, SOX).
- **Costo operativo**: Optimización de rutas y asignación de recursos para reducir costos logísticos.

## Opciones consideradas

> Preguntas guía:
> - ¿Qué alternativas arquitectónicas evalúas para resolver el contexto logístico?
> - ¿Cómo abordarías la integración con sistemas externos (ERP, TMS, pasarela de pagos)?
> - ¿Qué patrones de diseño considerarías para manejar la consistencia en un entorno distribuido?
> - ¿Qué estrategias de escalabilidad implementarías para manejar los picos de demanda?

(En blanco: lista y analiza las opciones)

## Decisión

> Preguntas guía:
> - ¿Qué arquitectura eliges y con qué criterios medibles?
> - ¿Cómo garantizarás el cumplimiento de los ASRs (rendimiento, escalabilidad, disponibilidad)?
> - ¿Qué herramientas o tecnologías utilizarías para implementar la solución?

(En blanco)

## Consecuencias

> Preguntas guía:
> - ¿Qué impacto tendrá la decisión en los ASRs?
> - ¿Qué riesgos adicionales introduce la solución y cómo los mitigarías?
> - ¿Cómo afectará la solución a la mantenibilidad y evolución futura de la plataforma?

(En blanco)

// === ARCHIVO: adr/002-diseno-arquitectonico.md ===
# ADR 002: Diseño Arquitectónico de la Plataforma Logística

Estado: Propuesto
Fecha: 2025-MM-DD

## Contexto

El diseño arquitectónico debe soportar los siguientes requisitos:

- **Descomposición modular**: Permitir escalar componentes individuales (ej: procesamiento de pedidos, gestión de inventario).
- **Integración con sistemas externos**: ERP (SAP), TMS, pasarela de pagos y geolocalización.
- **Tolerancia a fallos**: Manejar indisponibilidad de sistemas externos sin afectar la experiencia del usuario.
- **Consistencia eventual**: Garantizar que los datos de inventario y estado de pedidos converjan en un tiempo aceptable.
- **Visibilidad operativa**: Monitoreo en tiempo real del estado de pedidos y rutas.

El sistema actual es un monolito con las siguientes limitaciones:
- Acoplamiento alto entre componentes.
- Dificultad para escalar horizontalmente.
- Tiempo de despliegue prolongado (30 minutos).
- Falta de aislamiento de fallos.

## Fuerzas

- **Tensión entre modularidad y complejidad**: Descomponer el sistema en servicios independientes aumenta la complejidad operativa.
- **Latencia en comunicaciones**: Las integraciones con sistemas externos introducen latencia variable.
- **Consistencia de datos**: La replicación de datos entre servicios puede generar inconsistencias temporales.
- **Seguridad**: Protección de datos sensibles (información de clientes, pagos) en un entorno distribuido.
- **Costo de infraestructura**: Balance entre escalabilidad y costos operativos (ej: uso de colas vs. llamadas síncronas).

## Opciones consideradas

> Preguntas guía:
> - ¿Qué estilo arquitectónico (monolito, microservicios, SOA) es más adecuado para este dominio?
> - ¿Qué patrones de integración (event-driven, API Gateway, BFF) evaluarías para conectar los servicios?
> - ¿Cómo manejarías la consistencia de datos en un entorno distribuido?
> - ¿Qué estrategias de tolerancia a fallos implementarías para sistemas externos?
> - ¿Qué herramientas de observabilidad y monitoreo considerarías?

(En blanco: lista y analiza las opciones)

## Decisión

> Preguntas guía:
> - ¿Qué arquitectura eliges y con qué justificación técnica?
> - ¿Cómo organizarias los servicios y qué responsabilidades asignarías a cada uno?
> - ¿Qué tecnologías y patrones utilizarías para implementar la solución?
> - ¿Cómo garantizarías el cumplimiento de los ASRs (rendimiento, escalabilidad, disponibilidad)?

(En blanco)

## Consecuencias

> Preguntas guía:
> - ¿Qué impacto tendrá la decisión en los ASRs y en la operatividad del sistema?
> - ¿Qué riesgos introduce la solución y cómo los mitigarías?
> - ¿Cómo afectará la solución a la mantenibilidad y evolución futura de la plataforma?
> - ¿Qué métricas utilizarías para validar el éxito de la implementación?

(En blanco)

// === ARCHIVO: diagramas/contexto.mmd ===
```mermaid
%% Diagrama C4 - Contexto
%% Contexto del sistema logístico con actores y sistemas externos
%% NO incluir soluciones propuestas (to-be) — solo relaciones actuales

title Plataforma Logística - Diagrama de Contexto

actor Cliente as cliente
actor Proveedor as proveedor
actor Transportista as transportista
actor "Centro de Distribución" as centro_distribucion

system "Plataforma Logística" as plataforma {
    %% Este bloque representa el sistema actual (monolito)
    %% NO descomponer en servicios — solo relaciones externas
}

system_Ext ERP as erp "SAP"
system_Ext TMS as tms "Sistema de Gestión de Transportes"
system_Ext "Pasarela de Pagos" as pasarela_pagos "Stripe"
system_Ext "Geolocalización" as geolocalizacion "Google Maps API"

%% Relaciones
cliente --> plataforma : "Realiza pedidos"
proveedor --> plataforma : "Suministra inventario"
plataforma --> tms : "Coordina envíos"
plataforma --> pasarela_pagos : "Procesa pagos"
plataforma --> geolocalizacion : "Obtiene rutas"
plataforma --> centro_distribucion : "Gestiona inventario"
transportista --> tms : "Reporta estatus de envíos"

%% Leyenda
%% Preguntas guía para completar el diagrama:
%% - ¿Qué otros actores o sistemas externos faltan en este contexto?
%% - ¿Qué relaciones adicionales existen entre estos actores y sistemas?
%% - ¿Qué información fluye en cada relación? (ej: ID de pedido, estado de envío)
%% - ¿Qué sistemas externos tienen dependencias críticas con la plataforma?


// === ARCHIVO: poc/README.md ===
# Spike: Plataforma Logística

Este spike representa el **sistema actual** de la plataforma logística con el problema arquitectónico que el reto pide resolver:
- **Acoplamiento directo** entre los servicios de pedidos, envíos y rutas.
- **Falta de tolerancia a fallos** en las comunicaciones entre servicios.
- **Inconsistencia eventual** en el estado de los envíos.

El candidato debe **refactorizar este código** para:
1. Introducir una capa de orquestación que maneje la comunicación entre servicios.
2. Implementar el patrón **Outbox** para garantizar consistencia eventual.
3. Añadir mecanismos de **reintento y circuit breaker** en las comunicaciones.

## Instrucciones para ejecutar

1. Instalar dependencias:
   ```bash
   pip install fastapi uvicorn httpx python-multipart
   ```

2. Ejecutar el servicio:
   ```bash
   uvicorn poc.api-gateway-service.main:app --reload
   ```

3. Probar los endpoints:
   - Crear pedido: `POST /pedidos`
   - Consultar envío: `GET /envios/{envio_id}`
   - Cancelar envío: `GET /envios/{envio_id}/cancelar`

## Archivos incluidos
- `api-gateway-service/main.py`: Servicio principal con los endpoints y lógica actual.
- `docker-compose.yml`: Configuración para levantar servicios simulados (pedidos, envíos, rutas).

## Preguntas guía para el refactor
- ¿Cómo garantizarías la consistencia eventual entre los servicios sin acoplamiento directo?
- ¿Qué patrones usarías para manejar fallos en las comunicaciones entre servicios?
- ¿Cómo estructurarías la capa de orquestación para que sea escalable y mantenible?

--- **Nota**: El código actual contiene el problema que el reto pide resolver. No es una solución completa, sino un punto de partida para aplicar las mejoras arquitectónicas.

// === ARCHIVO: poc/docker-compose.yml ===
version: '3.8'

services:
  # Servicio de API Gateway (puerta de entrada)
  api-gateway:
    build:
      context: ./api-gateway-service
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    environment:
      - SERVICIO_PEDIDOS_URL=http://pedidos:8001
      - SERVICIO_ENVIOS_URL=http://envios:8002
      - SERVICIO_RUTAS_URL=http://rutas:8003
    depends_on:
      - pedidos
      - envios
      - rutas
    networks:
      - logistica-net

  # Servicio simulado de Pedidos
  pedidos:
    image: python:3.9-slim
    ports:
      - "8001:8001"
    volumes:
      - ./api-gateway-service/mock_services/pedidos.py:/app/main.py
    command: sh -c "pip install fastapi uvicorn && uvicorn main:app --host 0.0.0.0 --port 8001"
    networks:
      - logistica-net

  # Servicio simulado de Envíos
  envios:
    image: python:3.9-slim
    ports:
      - "8002:8002"
    volumes:
      - ./api-gateway-service/mock_services/envios.py:/app/main.py
    command: sh -c "pip install fastapi uvicorn && uvicorn main:app --host 0.0.0.0 --port 8002"
    networks:
      - logistica-net

  # Servicio simulado de Rutas
  rutas:
    image: python:3.9-slim
    ports:
      - "8003:8003"
    volumes:
      - ./api-gateway-service/mock_services/rutas.py:/app/main.py
    command: sh -c "pip install fastapi uvicorn && uvicorn main:app --host 0.0.0.0 --port 8003"
    networks:
      - logistica-net

networks:
  logistica-net:
    driver: bridge

// === ARCHIVO: poc/api-gateway-service/mock_services/pedidos.py ===
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
import uuid
import random

app = FastAPI()

class Pedido(BaseModel):
    producto_id: str
    cantidad: int
    direccion_entrega: str
    cliente_id: str

# Simulación de base de datos en memoria
pedidos_db: Dict[str, Dict[str, Any]] = {}

@app.post("/pedidos")
async def crear_pedido(pedido: Pedido) -> Dict[str, Any]:
    pedido_id = str(uuid.uuid4())
    pedidos_db[pedido_id] = {
        "producto_id": pedido.producto_id,
        "cantidad": pedido.cantidad,
        "direccion_entrega": pedido.direccion_entrega,
        "cliente_id": pedido.cliente_id,
        "estado": "CREADO"
    }
    # Simular fallo aleatorio en el 20% de los casos
    if random.random() < 0.2:
        raise HTTPException(status_code=500, detail="Error interno en el servicio de pedidos")
    return {"pedido_id": pedido_id, "estado": "CREADO"}

@app.get("/pedidos/{pedido_id}")
async def consultar_pedido(pedido_id: str) -> Dict[str, Any]:
    if pedido_id not in pedidos_db:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedidos_db[pedido_id]

// === ARCHIVO: poc/api-gateway-service/mock_services/envios.py ===
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
import uuid
import random

app = FastAPI()

class Envio(BaseModel):
    pedido_id: str
    direccion_entrega: str
    estado: str = "PENDIENTE"

# Simulación de base de datos en memoria
envios_db: Dict[str, Dict[str, Any]] = {}

@app.post("/envios")
async def crear_envio(envio: Envio) -> Dict[str, Any]:
    envio_id = str(uuid.uuid4())
    envios_db[envio_id] = {
        "pedido_id": envio.pedido_id,
        "direccion_entrega": envio.direccion_entrega,
        "estado": envio.estado
    }
    # Simular fallo aleatorio en el 20% de los casos
    if random.random() < 0.2:
        raise HTTPException(status_code=500, detail="Error interno en el servicio de envíos")
    return {"envio_id": envio_id, "estado": envio.estado}

@app.get("/envios/{envio_id}")
async def consultar_envio(envio_id: str) -> Dict[str, Any]:
    if envio_id not in envios_db:
        raise HTTPException(status_code=404, detail="Envío no encontrado")
    return envios_db[envio_id]

@app.put("/envios/{envio_id}/cancelar")
async def cancelar_envio(envio_id: str) -> Dict[str, Any]:
    if envio_id not in envios_db:
        raise HTTPException(status_code=404, detail="Envío no encontrado")
    envios_db[envio_id]["estado"] = "CANCELADO"
    return {"envio_id": envio_id, "estado": "CANCELADO"}

// === ARCHIVO: poc/api-gateway-service/mock_services/rutas.py ===
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
import uuid
import random

app = FastAPI()

class Ruta(BaseModel):
    envio_id: str
    origen: str
    destino: str
    estado: str = "PLANIFICADA"

# Simulación de base de datos en memoria
rutas_db: Dict[str, Dict[str, Any]] = {}

@app.post("/rutas")
async def crear_ruta(ruta: Ruta) -> Dict[str, Any]:
    ruta_id = str(uuid.uuid4())
    rutas_db[ruta_id] = {
        "envio_id": ruta.envio_id,
        "origen": ruta.origen,
        "destino": ruta.destino,
        "estado": ruta.estado
    }
    # Simular fallo aleatorio en el 20% de los casos
    if random.random() < 0.2:
        raise HTTPException(status_code=500, detail="Error interno en el servicio de rutas")
    return {"ruta_id": ruta_id, "estado": ruta.estado}

@app.get("/rutas/{ruta_id}")
async def consultar_ruta(ruta_id: str) -> Dict[str, Any]:
    if ruta_id not in rutas_db:
        raise HTTPException(status_code=404, detail="Ruta no encontrada")
    return rutas_db[ruta_id]

// === ARCHIVO: poc/api-gateway-service/Dockerfile ===
FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn httpx python-multipart

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```
