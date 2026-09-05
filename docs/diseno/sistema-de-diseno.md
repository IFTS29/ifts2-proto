# Sistema de Diseño y Arquitectura de Información Web: IFTS N° 2

## Fusión Institucional: Identidad IFTS (CABA) + Excelencia Curricular (Benchmark Azafrán)

---

## 1. Análisis de Benchmark y Filosofía de Fusión

### 1.1 El Ecosistema IFTS en CABA
El relevamiento de los sitios de referencia de la Red de Institutos de Formación Técnica Superior de la Ciudad de Buenos Aires (**IFTS 18, IFTS 27, IFTS 11, IFTS 7, IFTS 20, IFTS 21, IFTS 13**) arroja patrones identitarios y funcionales constantes:
1. **Identidad "IFTS" Protagónica:** El nombre, número y condición de institución pública terciaria ("IFTS N° 2 - D.E. 20") encabeza la jerarquía visual con el respaldo oficial del Gobierno de la Ciudad (Ministerio de Educación / DGEST / Agencia de Aprendizaje a lo Largo de la Vida).
2. **Sobriedad y Claridad Visual:** Predominan los fondos blancos y grises claros (`#ffffff`, `#f8fafc`), con tipografías legibles y colores institucionales (azul marino, azul institucional, pizarra) que transmiten seriedad, confianza y rigor académico. Se evitan estéticas nocturnas, sobrecargadas o de estética comercial de restaurante/bar.
3. **Servicios al Estudiante y Trámites Centrales:** Acceso inmediato y visible a herramientas cotidianas: **SIU-Guaraní**, Calendario Académico, Solicitud de Certificados, Régimen de Correlatividades, Exámenes Libres, Equivalencias y Bedelía.
4. **Ingreso Oficial GCBA:** Información transparente sobre fechas, instructivos de inscripción oficial y gratuidad absoluta (títulos de validez nacional).

### 1.2 La Aportación de Azafrán Escuela de Gastronomía
Del benchmark de **Azafrán Escuela de Gastronomía** se rescata la modernidad y el dinamismo pedagógico:
* **Ficha Técnica de Carrera de Alto Impacto:** Duración (3 años), modalidad, turno y salida laboral presentadas con síntesis ejecutiva.
* **Perfil Profesional Diferenciado:** *"No formamos cocineros rasos, formamos empresarios y gestores gastronómicos"*.
* **Plan de Estudios Dinámico e Interactivo:** Desglose año a año con materias técnicas y de negocios.
* **Ventana Viva al Aprendizaje Práctico:** Galería/carrusel de producciones reales, eventos y masterclasses sin desvirtuar la institucionalidad.

### 1.3 La Fórmula de Fusión para el IFTS N° 2
> **Fórmula:** *El rigor, la sobriedad y la arquitectura de servicios de un IFTS oficial de CABA + la modernidad editorial, la claridad curricular y la exhibición de prácticas de Azafrán.*

---

## 2. Sistema de Diseño Visual (Soberbio, Limpio y Accesible)

Para evitar estéticas excesivamente coloridas o nocturnas, se adopta una paleta institucional limpia, con alto contraste y certificación WCAG 2.1 AA.

### 2.1 Paleta Cromática Institucional

| Rol de Color | Tono / Código HEX | Uso en la Interfaz |
| :--- | :--- | :--- |
| **Azul Marino Institucional** | `#1e3a8a` (Blue 900) / `#0f2942` | Encabezado principal, títulos de sección, enlaces primarios y pie de página institucional. |
| **Azul Primario GCBA** | `#0284c7` (Sky 600) / `#2563eb` | Botones de acción principal (Inscripción, SIU Guaraní), tabs activos y focos de interacción. |
| **Fondos de Superficie** | `#ffffff` (Blanco Puro) / `#f8fafc` (Slate 50) | Fondo general del sitio, tarjetas de contenido y paneles de lectura descansada. |
| **Gris Institucional de Apoyo** | `#f1f5f9` (Slate 100) / `#e2e8f0` (Slate 200) | Fondos de bloques alternos, divisores de sección y bordes de tarjetas. |
| **Tipografía Principal** | `#0f172a` (Slate 900) / `#334155` (Slate 700) | Textos de cuerpo, subtítulos y datos con máximo contraste legible. |
| **Acento Cálido Gastronómico (Medido)** | `#b45309` (Amber 700) / `#d97706` | Pinceladas exclusivas en insignias de la carrera, horas de práctica y etiquetas destacadas. No satura. |

### 2.2 Tipografía
* **Familia Tipográfica Principal:** `Inter` o `Plus Jakarta Sans` para todo el sistema (cabeceras, menús y textos). Son tipografías sans-serif neutras, de legibilidad óptima en pantalla y utilizadas en los portales gubernamentales y universitarios modernos.
* **Escala y Jerarquía:**
  * **Título Institucional (Hero / IFTS):** 36px – 44px (`font-bold`, leading ceñido).
  * **Títulos de Sección (H2):** 24px – 28px (`font-semibold`, Slate 900).
  * **Subtítulos y Bloques (H3):** 18px – 20px (`font-semibold`, Blue 900).
  * **Cuerpo de Texto:** 15px – 16px (`font-normal`, Slate 700, `leading-relaxed`).
  * **Insignias y Metadatos:** 12px – 13px (`font-medium` o `font-semibold`, tracking suave).

---

## 3. Arquitectura de Información

La estructura equilibra las necesidades de **Aspirantes** y de **Estudiantes Actuales**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. BARRA SUPERIOR GCBA: Ministerio de Educación | DGEST | Validez Nacional  │
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. HEADER INSTITUCIONAL:                                                    │
│    [Logo GCBA] IFTS N° 2 D.E. 20                                            │
│    Menú: Institucional | Carrera | Alumnos & SIU | Ingreso | Comunidad IG   │
│    Botón CTA: Portal SIU-Guaraní / Pre-inscripción                          │
├─────────────────────────────────────────────────────────────────────────────┤
│ 3. HERO INSTITUCIONAL + FORMATIVO:                                          │
│    - Título: Instituto de Formación Técnica Superior N° 2                   │
│    - Subtítulo: Tecnicatura Superior en Emprendimientos Gastronómicos       │
│    - Eje: "Educación pública, gratuita y con visión empresarial"            │
│    - Ficha técnica: 3 años | Turno Noche (18:30 a 22:30) | Validez Nacional │
│    - Accesos Rápidos: [Plan de Estudios] [Requisitos de Ingreso] [Trámites] │
├─────────────────────────────────────────────────────────────────────────────┤
│ 4. ACCESO RÁPIDO PARA ALUMNOS (Estilo IFTS 18 / IFTS 27):                   │
│    [SIU Guaraní] [Calendario 2026] [Certificados] [Régimen / Equivalencias] │
├─────────────────────────────────────────────────────────────────────────────┤
│ 5. LA CARRERA: PERFIL DEL EGRESADO (Inspirado en Azafrán):                  │
│    - Gestión Económico-Financiera de Negocios Gastronómicos                 │
│    - Dirección de Operaciones y Brigadas de Cocina                          │
│    - Seguridad e Inocuidad Alimentaria (Bromatología)                       │
│    - Marketing Gastronómico, Franquicias y Eventos                          │
├─────────────────────────────────────────────────────────────────────────────┤
│ 6. PLAN DE ESTUDIOS INTERACTIVO:                                            │
│    - Tabs: 1° Año | 2° Año | 3° Año (con correlatividades y 160h prácticas) │
├─────────────────────────────────────────────────────────────────────────────┤
│ 7. PRÁCTICAS PROFESIONALIZANTES & COMUNIDAD (Instagram Curado):             │
│    - Título: Vida Institucional, Clases Magistrales y Producción Real       │
│    - Filtros: Todos | Emprendimientos | Masterclasses | Prácticas | Eventos │
│    - Carrusel 1:1 con apertura en Modal y enlace al post oficial            │
├─────────────────────────────────────────────────────────────────────────────┤
│ 8. INGRESO Y PREINSCRIPCIÓN:                                                │
│    - Proceso paso a paso vía Sistema de Inscripciones CABA                  │
│    - Fechas oficiales y documentación requerida                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 9. BEDELÍA Y TRÁMITES FRECUENTES:                                           │
│    - Horarios de atención presencial, correo de Bedelía, preguntas frecuentes│
├─────────────────────────────────────────────────────────────────────────────┤
│ 10. FOOTER INSTITUCIONAL:                                                   │
│     - Dirección (Comuna 9 / D.E. 20, CABA), mapa, contacto y redes oficiales│
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Especificación UI del Carrusel de Instagram (@ifts2de20)

### 4.1 Criterio de Curaduría Editorial
Tal como solicitaron las autoridades del instituto en la reunión de relevamiento, **no se debe volcar un feed social sin filtro**, sino exhibir selectivamente el valor formativo y profesionalizante del IFTS:
* **Contenido admitido:** Masterclasses de especialistas, prácticas en cocina de brigada, proyectos de graduación/emprendimientos de estudiantes, convenios y visitas técnicas, actos de colación y eventos institucionales (ej. Concurso de Guisos Criollos, participación en ferias gastronómicas).
* **Contenido descartado:** Memes, historias efímeras o avisos informales no académicos.

### 4.2 Formato y Comportamiento del Componente
* **Relación de Aspecto:** 1:1 uniforme (cuadrado perfecto).
* **Interacción:**
  * Vista previa limpia con insignia de categoría institucional y fecha del post.
  * Al pasar el mouse o recibir foco por teclado, se muestra un extracto del pie de foto y métricas de interacción.
  * Al hacer clic, se despliega un **Modal / Lightbox accesible** que permite leer el texto completo del post, ver la imagen en alta definición y acceder directamente al enlace verificado en Instagram.
* **Controles:** Botones de desplazamiento horizontal anterior/siguiente y filtros temáticos por botones tipo pastilla (chips).
