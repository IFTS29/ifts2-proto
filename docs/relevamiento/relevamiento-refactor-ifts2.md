# Relevamiento para refactor del sitio del IFTS N°2 DE 20

Fuente del sitio actual: https://sites.google.com/bue.edu.ar/ifts-2-de-20/página-principal
Fecha de la reunión: 04/09/2026

---

## 1. Estructura actual del sitio (Google Sites)

El sitio tiene 8 secciones en el menú principal. Todas comparten el mismo header/footer (logo, teléfono, mail, dirección) y no tienen ninguna otra navegación interna.

| Página | Contenido actual | Problema principal |
|---|---|---|
| **Página principal** | Feed cronológico descendente de noticias/eventos desde 2021 hasta 2025 (Guiso Fest, toma de posesión de rectora, mateadas, jornadas gastronómicas, cierres de cuatrimestre, comunicados institucionales, llamados a concurso docente) mezclado con videos e imágenes | Es un "muro" infinito sin archivar; información vieja (2021-2022) al mismo nivel que la actual; mezcla eventos, noticias institucionales y avisos administrativos sin categorizar |
| **Docentes** | 2 archivos descargables (modelo de programa, modelo de plan de clase) | Casi vacía, sin distinguir por materia/año |
| **Alumnos** | Lista larga y cronológica de horarios, mesas de examen, agendas (2021 a 2026), links a SIU Guaraní y Moodle | Mismo problema de archivo: 5 años de xlsx/pdf sueltos sin buscador ni filtro por año |
| **Ingreso 2025** | (no relevado en detalle) | — |
| **Información Académica** | Título oficial, resolución, plan de estudios, correlatividades, listado de materias, plantel docente | Es de las páginas mejor estructuradas, pero todo son PDFs/Docs externos, no contenido navegable |
| **Tutoría** | (no relevado en detalle) | — |
| **¿Dónde estamos?** | (no relevado en detalle, probablemente mapa/dirección) | — |
| **Galería de imágenes** | (no relevado en detalle) | — |
| **Redes sociales** | (no relevado en detalle, probablemente links a Facebook/Instagram) | — |

**Diagnóstico general del sitio actual:**
- No hay separación entre "información estática" (plan de estudios, correlatividades, autoridades) e "información dinámica" (eventos, novedades, horarios del cuatrimestre vigente).
- No hay archivo/histórico: todo el contenido de años anteriores queda visible y mezclado con lo vigente.
- Fuerte dependencia de archivos sueltos (PDF, DOCX, XLSX) en vez de contenido en la propia página.
- Sin buscador, sin filtros, sin categorías por año/temática.
- Sin canal de contacto formal más allá de un mail genérico.

---

## 2. Notas de la reunión de refactor (04/09/2026)

### 2.1 Participantes / stakeholders
- **Cecilia** — Rectora
- **María** — Gastronomía
- **Matías Peláez** — Profesor
- **Asistente pedagógica** (sin nombre registrado)
- **Héctor** — Asesor
- **Mario** — solicita un canal de contacto formal

### 2.2 Definiciones y lineamientos acordados
- Trabajar sobre la **página oficial** existente y **modernizarla / innovar**, no partir de cero.
- Se compartirá una carpeta de **Drive con documentación** de referencia.
- Limitante mencionada: **falta de tiempo** del equipo docente/directivo para producir contenido.
- **Redes sociales**: lo que se publique en redes debe ser **selectivo** antes de subirlo a la web — no todo lo que va a redes va al sitio.
- Se pidió definir **qué subir y qué no subir al sitio** (criterio de selección de contenido).
- Evaluar si conviene **armar una página aparte que no sea el sitio oficial** para cierto contenido (por ejemplo, para lo más informal o efímero).

### 2.3 Requerimientos funcionales relevados

**Gestión de contenido**
- Selección de información de Instagram para mostrar en la página (curaduría, no volcado automático).
- Rollover / hover de información (interacción para mostrar detalle sin recargar la página).
- Archivar información vieja (histórico separado del contenido vigente).
- Repositorio de archivos (centralizar PDFs/DOCs/XLSX en un solo lugar ordenado).
- Mostrar información de eventos organizados por temática y por año.
- Información estática vs. dinámica claramente diferenciada.

**Restricciones**
- Costos limitados (la solución debe ser económica de mantener/alojar).
- Se evaluaron opciones de **alojamiento gratuito** (".edu" mencionado como pista a investigar — alojamiento gratuito para instituciones educativas).

**Contenido institucional a incluir (requerimientos IFTS N°2)**
- Plan de Carrera Institucional
- Perfil del Egresado — **eje central pedido explícitamente**: *"No formamos chefs, formamos empresarios gastronómicos"*
- Correlatividades de materias
- Autoridades (con posibilidad de edición fácil / editable)
- Historial de horarios
- Galería de imágenes (con filtro)
- Link al SIU (inscripción a la tecnicatura)
- Link a Aulas Virtuales (Moodle)
- Link a "Mi Argentina" (revisar validez del título)
- Formulario de contacto → bedelía (mail)
- Trámites frecuentes
- Simulador gastronómico (a futuro / feature planeada, no para el MVP)
- Sección de **Eventos**, agrupando:
  - Mateada Patria (dejar solo la última edición visible, no todas)
  - Cierre de 1º cuatrimestre
  - Colación (evento anual, una vez al año)
  - Jornada de gastronomía
  - Participación en la Noche de los Museos

### 2.4 Notas sueltas / a definir
- Definir qué pasa con el contenido que hoy está en el "más" del menú (Ingreso, Tutoría, Dónde estamos, Galería, Redes sociales) — no quedó relevado en detalle en las notas.
- Está pendiente decidir la plataforma final (Google Sites actual vs. stack propio) considerando el punto de costos y de "alojamiento gratuito".

---

## 3. Propuesta de reorganización de la información (a partir del cruce sitio + notas)

1. **Institucional (estático)** — Plan de carrera, Perfil del egresado, correlatividades, autoridades, plantel docente, resoluciones/normativa.
2. **Académico (semi-dinámico, por ciclo lectivo)** — Horarios vigentes, mesas de examen vigentes, materias por año/cuatrimestre, trámites frecuentes, links a SIU/Moodle/Mi Argentina.
3. **Eventos (dinámico, con archivo)** — Eventos del año en curso destacados arriba; eventos anteriores archivados por año, filtrables por temática.
4. **Novedades/Redes** — Selección curada de contenido de Instagram, no volcado automático; criterio explícito de qué sube y qué no.
5. **Repositorio de archivos** — Un único lugar central para todos los PDF/DOCX/XLSX, en vez de dispersos en cada página.
6. **Contacto** — Formulario a bedelía + canal de contacto formal (pedido de Mario).

Esta separación resuelve directamente los dos problemas más repetidos en las notas: **archivar lo viejo** y **diferenciar estático de dinámico**.

---

*Nota: las secciones "Ingreso 2025", "Tutoría", "¿Dónde estamos?", "Galería de imágenes" y "Redes sociales" del sitio actual no se relevaron en detalle en esta pasada — si las necesitás para el trabajo final, las reviso también.*
