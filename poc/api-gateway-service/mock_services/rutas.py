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