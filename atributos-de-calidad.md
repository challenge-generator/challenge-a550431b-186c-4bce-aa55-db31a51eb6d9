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