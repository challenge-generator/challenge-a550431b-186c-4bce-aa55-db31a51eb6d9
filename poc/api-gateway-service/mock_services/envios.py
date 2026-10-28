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