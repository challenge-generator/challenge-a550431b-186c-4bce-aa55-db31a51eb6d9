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