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