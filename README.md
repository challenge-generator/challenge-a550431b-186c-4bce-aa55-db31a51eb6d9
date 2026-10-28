# Diseño y Evaluación de Arquitectura para Plataforma Logística

El candidato debe liderar el diseño y evaluación técnica de una plataforma logística, facilitando una sesión de Event Storming, definiendo el mapa de contextos con DDD, aplicando iteraciones de diseño con ADD 3.0 y realizando una evaluación formal ATAM para documentar los riesgos de rendimiento y escalabilidad.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Metodologías y frameworks para diseño y evaluación de arquitectura de software |
| **Nivel** | advanced-l3 |
| **Tipo** | mixed |
| **Tiempo estimado** | 180 minutos |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Facilitar Sesión de Event Storming

**Objetivo:** Generar insights y eventos clave del dominio logístico

**Tiempo estimado:** 30 minutos

**Instrucciones:**

- Facilitar una sesión de Event Storming para identificar eventos y procesos clave en la logística.
- Documentar los eventos identificados y sus relaciones.

**Entregable:** Mapa de eventos y procesos logísticos.

<details>
<summary>Pistas de conocimiento</summary>

- Event Storming es una técnica para descubrir eventos relevantes en un dominio.
- Identifica eventos, comandos y agregados.

</details>

### Fase 2: Definir Mapa de Contextos con DDD

**Objetivo:** Establecer los límites y contextos de la plataforma logística

**Tiempo estimado:** 30 minutos

**Instrucciones:**

- Definir los contextos acotado y compartidos utilizando DDD.
- Identificar los límites y responsabilidades de cada contexto.

**Entregable:** Mapa de contextos DDD para la plataforma logística.

<details>
<summary>Pistas de conocimiento</summary>

- DDD ayuda a modelar el dominio en contextos acotados.
- Cada contexto debe tener una responsabilidad clara.

</details>

### Fase 3: Aplicar Iteraciones de Diseño con ADD 3.0

**Objetivo:** Iterar en el diseño de la arquitectura utilizando ADD 3.0

**Tiempo estimado:** 60 minutos

**Instrucciones:**

- Aplicar el método ADD 3.0 para iterar en el diseño de la arquitectura.
- Identificar y evaluar opciones de diseño, considerando trade-offs.

**Entregable:** Documento de diseño iterativo utilizando ADD 3.0.

<details>
<summary>Pistas de conocimiento</summary>

- ADD 3.0 es un método para diseñar arquitecturas de software.
- Considera trade-offs y evaluaciones de alternativas.

</details>

### Fase 4: Realizar Evaluación Formal ATAM

**Objetivo:** Documentar riesgos de rendimiento y escalabilidad

**Tiempo estimado:** 60 minutos

**Instrucciones:**

- Realizar una evaluación formal ATAM para identificar y documentar riesgos de rendimiento y escalabilidad.
- Preparar un informe con los hallazgos y recomendaciones.

**Entregable:** Informe de evaluación ATAM con hallazgos y recomendaciones.

<details>
<summary>Pistas de conocimiento</summary>

- ATAM es un método para evaluar la arquitectura de software.
- Identifica y documenta riesgos y recomendaciones.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es Event Storming y cómo se aplica en el diseño de arquitectura?
- **paraQueSirve**: ¿Para qué sirve el diseño dirigido por dominio (DDD) en la arquitectura de software?
- **comoSeUsa**: ¿Cómo se utiliza el método ADD 3.0 para iterar en el diseño de la arquitectura?
- **erroresComunes**: ¿Cuáles son los errores comunes al aplicar metodologías de diseño de arquitectura?
- **queDecisionesImplica**: ¿Qué decisiones implica la realización de una evaluación formal ATAM?

## Criterios de Evaluacion

- Alineación del diseño con los requisitos arquitectónicos significativos (ASRs).
- Uso justificado de patrones y herramientas frente a alternativas.
- Calidad de los diagramas y del documento de arquitectura con trade-offs explícitos.
- Viabilidad y madurez del diseño (seguridad, observabilidad y operación realista).

## Como trabajar con un asistente de IA

Hay dos caminos, elegi uno:

- **AGENTS.md** (recomendado) — instrucciones nativas del repo. Abri esta carpeta con tu agente local (Claude Code, Cursor, Codex, Copilot, Gemini) y las carga solo. Sabe que archivos faltan y con que comando se verifica, y completa el scaffold escribiendo en disco.
- **PROMPT_MEJORA.md** — para copiar y pegar en un chat (claude.ai, ChatGPT). Devuelve un ZIP con el proyecto. Sirve si no tenes un agente en el IDE.

Ninguno de los dos resuelve las fases del reto: eso es tu trabajo.

## Verificacion

El proyecto esta listo para trabajar cuando este comando corre sin errores:

```bash
python3 -c "import glob,sys; assert glob.glob('adr/*.md') and glob.glob('diagramas/*.mmd'), 'faltan ADRs o diagramas'"
```

---

*Reto generado automaticamente por Challenge Generator - Pragma*
