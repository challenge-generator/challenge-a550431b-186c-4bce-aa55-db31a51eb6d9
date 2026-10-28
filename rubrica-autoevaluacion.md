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