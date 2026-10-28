# AGENTS.md

Instrucciones para el agente de IA que abra este repositorio (Claude Code, Cursor, Codex, Copilot, Gemini). Se cargan solas: no hay que pegar nada en ningun chat.

## Que es este repositorio

Es el codigo base de un reto de aprendizaje de Pragma: **Diseño y Evaluación de Arquitectura para Plataforma Logística**.

| | |
|---|---|
| Tema | Metodologías y frameworks para diseño y evaluación de arquitectura de software |
| Nivel | advanced-l3 |
| Chapter | Arquitectura |
| Especialidad | Soluciones |
| Stack | Markdown / C4 Model + ADR + ADD 3.0 + ATAM |
| Patron arquitectonico | Documentación arquitectónica basada en vistas C4, ADRs y evaluación formal con ATAM |
| Tiempo estimado | 180 minutos |

## Receta del stack

Esqueleto obligatorio:

- `adr/`
- `arquitectura.md`
- `diagramas/*.mmd`
- `atributos-de-calidad.md`
- `rubrica-autoevaluacion.md`
- `poc/ (opcional)`

Dependencias:

- Mermaid.js 10.9.0
- C4 Model n/a
- ADD 3.0 (Attribute-Driven Design) n/a
- ATAM (Architecture Tradeoff Analysis Method) n/a
- PlantUML 1.2023.12

## Tu tarea

Dejar este conjunto de artefactos en estado **verificable**: que el comando de verificacion corra sin errores. Escribi los archivos en disco, en este repositorio. No generes ZIPs ni archivos adjuntos.

En orden:

1. Corre `python3 -c "import glob,sys; assert glob.glob('adr/*.md') and glob.glob('diagramas/*.mmd'), 'faltan ADRs o diagramas'"` y mira que falla.
2. Completa lo que falte de la lista de abajo: manifiesto de dependencias, punto de entrada, capa de interfaz y las capas del patron declarado.
3. Arregla SOLO los errores que impiden compilar o arrancar.
4. Volve a correr `python3 -c "import glob,sys; assert glob.glob('adr/*.md') and glob.glob('diagramas/*.mmd'), 'faltan ADRs o diagramas'"` hasta que pase.
5. Pará ahí.

## Regla dura: las fases son trabajo del humano

**PROHIBIDO implementar los entregables de las fases.** El valor del reto esta en que la persona los resuelva. Tu trabajo es que tenga un proyecto que arranca; el hueco pedagogico se queda como esta.

No resuelvas nada de esto:

- **Fase 1 — Facilitar Sesión de Event Storming**: Mapa de eventos y procesos logísticos.
- **Fase 2 — Definir Mapa de Contextos con DDD**: Mapa de contextos DDD para la plataforma logística.
- **Fase 3 — Aplicar Iteraciones de Diseño con ADD 3.0**: Documento de diseño iterativo utilizando ADD 3.0.
- **Fase 4 — Realizar Evaluación Formal ATAM**: Informe de evaluación ATAM con hallazgos y recomendaciones.

Distincion operativa:

- **Arreglar** (si): import faltante, tipo que no existe, dependencia sin declarar, error de sintaxis, archivo referenciado que no existe.
- **No tocar** (no): logica de negocio incompleta, validaciones ausentes, secretos hardcodeados, APIs deprecadas que funcionan, concurrencia insegura, patrones mejorables. Eso es lo que la persona tiene que encontrar.

## Superficie de practica (NO completes)

Estos archivos SON el ejercicio de la persona. No los implementes; deja stubs. No toques la logica que el reto pide completar.

- [ ] `adr/001-contexto-logistico.md` — El topic pide decisiones de arquitectura: el ADR es el ejercicio.
- [ ] `adr/002-diseno-arquitectonico.md` — El topic pide decisiones de arquitectura: el ADR es el ejercicio.

## Lo que falta y tenes que completar

No se detectaron huecos: estan los archivos declarados, el boilerplate del stack y ninguna referencia quedo colgando. Igual corre el comando de verificacion — que los archivos existan no garantiza que compilen.

### Presentes (15)

- `poc/api-gateway-service/main.py`
- `arquitectura.md`
- `README.md`
- `atributos-de-calidad.md`
- `riesgos-y-mitigaciones.md`
- `rubrica-autoevaluacion.md`
- `adr/001-contexto-logistico.md`
- `adr/002-diseno-arquitectonico.md`
- `diagramas/contexto.mmd`
- `poc/README.md`
- `poc/docker-compose.yml`
- `poc/api-gateway-service/mock_services/pedidos.py`
- `poc/api-gateway-service/mock_services/envios.py`
- `poc/api-gateway-service/mock_services/rutas.py`
- `poc/api-gateway-service/Dockerfile`

### Capas del patron declarado

Cada una tiene que existir como directorio real con al menos un archivo. Codigo plano en la raiz no satisface el patron.

- `adr`
- `diagramas`
- `evaluacion`
- `contextos`
- `event-storming`

## Verificacion

```bash
python3 -c "import glob,sys; assert glob.glob('adr/*.md') and glob.glob('diagramas/*.mmd'), 'faltan ADRs o diagramas'"
```

El comando tiene que pasar SIN implementar los archivos de la superficie de practica: solo andamiaje.

Ese comando pasando es la definicion de "terminado" para vos.

## Convenciones que tenes que respetar

- Un solo ecosistema: no declares librerias de otro lenguaje ni mezcles gestores de paquetes.
- Toda libreria que uses tiene que estar declarada en el manifiesto de dependencias.
- Todo import declarado tiene que usarse; todo tipo usado tiene que existir o venir de una dependencia declarada.
- El patron es **Documentación arquitectónica basada en vistas C4, ADRs y evaluación formal con ATAM**: los contratos (interfaces, puertos) los define la capa interna y los implementa la externa, nunca al revés.
- Los archivos que crees llevan implementacion real, no stubs: sin `TODO`, sin cuerpos vacios, sin `// getters y setters`.

## Contexto del candidato

Sirve para calibrar el nivel del codigo, no para resolver las fases.

- Perfil: Chapter Arquitectura, Especialidad Soluciones, Advanced
- Brecha que el reto ataca: Entiende, aplica y sigue una metodología para el diseño de Arquitectura, toma decisiones de arquitectura y acompaña su salida a producción, comprende y aplica metodologías y framework como ADD, DDD y métodos de evaluación como ATAM y SAAM, también sabe usar event storming
- Mision: Candidato con experiencia aplicando DDD y ADD en arquitecturas complejas de microservicios, integraciones con sistemas legados, y evaluación de trade-offs arquitectónicos.

---

*Generado por Challenge Generator — Pragma. `README.md` tiene el enunciado completo del reto para la persona. `PROMPT_MEJORA.md` es la variante para pegar en un chat, si se prefiere ese flujo.*
