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