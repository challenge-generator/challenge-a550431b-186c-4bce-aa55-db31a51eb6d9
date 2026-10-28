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