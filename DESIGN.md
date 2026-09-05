# Sistema de Diseño y Arquitectura Web: IFTS N° 2
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

## 4. Especificación del Carrusel de Instagram (@ifts2de20)

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

---

## 5. Arquitectura Técnica de Automatización para la Tesis (Costo $0)

### 5.1 Matriz de Decisión y Evaluación de Alternativas

| Criterio | Opción A: Embeds Manuales (iframes de Meta) | Opción B: Web Scraping no oficial | Opción C (Elegida): Instagram API with Instagram Login + CI/CD |
| :--- | :--- | :--- | :--- |
| **Nivel de Automatización** | Nulo (Manual: requiere pegar código post por post). | Alto, pero frágil (se rompe con cualquier cambio de HTML). | **Totalmente automatizado y desatendido.** |
| **Carga de Trabajo del IFTS** | Inviable (el equipo docente declaró no tener tiempo). | Nula. | **Mantenimiento CERO para el personal del IFTS.** |
| **Términos de Servicio (TOS)** | Aprobado. | Viola los términos de Meta (riesgo de baneo de IP). | **100% Oficial y en regla con Meta Developer TOS.** |
| **Estabilidad de Medios** | Alto impacto en performance (scripts pesados de terceros). | Alta tasa de fallo por bloqueo anti-bot. | **Imágenes cacheadas localmente: carga ultrarrápida.** |
| **Costo de Infraestructura** | $0 | $0 (hasta que bloquean IP y requiere proxies pagos). | **$0 / mes (Astro + GitHub Actions + Cloudflare Pages).** |

### 5.2 El Estándar de Meta en 2026: *Instagram API with Instagram Login*
1. **Discontinuación de Basic Display API (Diciembre 2024):** Meta dio de baja definitiva la antigua Basic Display API. La vía moderna oficial para cuentas propias es **Instagram API with Instagram Login** (`https://graph.instagram.com`).
2. **Sin vinculación de Página de Facebook:** A diferencia de la antigua ruta de Facebook Login (que exigía vincular una Fanpage y otorgar permisos complejos de administración), la nueva API permite autenticar directamente con las credenciales de la cuenta institucional de Instagram. Menos fricción y menos piezas que mantener.
3. **Acceso Estándar (Standard Access) sin App Review:**
   * Al ser un desarrollo para la propia institución (caso de uso "Own Account / Single Business"), **no se requiere la revisión avanzada comercial (App Review)** de Meta.
   * Alcanza con registrar la cuenta `@ifts2de20` en el rol de **Instagram Tester** dentro del panel de Meta for Developers. Esto permite consumir el endpoint `/me/media` con cuota oficial sin costo.
4. **Consumo de Cuota Despreciable:**
   * Límite de Meta: 200 llamadas por hora por usuario.
   * Consumo de nuestra solución: **1 a 2 llamadas diarias** (0.04% del límite de la cuota disponible).

### 5.3 Problema de Expiración de URLs y Solución Técnica (CDN/Repo Caching)
* **La trampa de `media_url`:** Las URLs de imágenes provistas por la API de Graph expiran tras 48 a 72 horas por razones de seguridad y privacidad de Meta. Si un sitio web estático las almacena tal cual, las imágenes se rompen a los pocos días.
* **Solución aplicada en el pipeline:** El script de sincronización descarga el archivo binario de cada imagen, lo optimiza a formato WebP moderno y lo persiste dentro del repositorio (`assets/instagram/`) o bucket de distribución estática. De este modo, el sitio web sirve sus propias imágenes locales con disponibilidad permanente del 100%.

### 5.4 Gestión Desatendida del Token de Larga Duración (Long-Lived Token)
* El token de larga duración de Meta tiene una validez de **60 días**.
* **Estrategia de auto-renovación:** Cada vez que el GitHub Action corre (diariamente), evalúa la antigüedad del token o invoca al endpoint de refresco:
  ```http
  GET https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token={LONG_LIVED_TOKEN}
  ```
* Al ejecutarse entre el día 30 y 45, el token se renueva por otros 60 días adicionales y actualiza de forma segura el Secret del repositorio vía GitHub API, logrando un ciclo perpetuo desatendido.

### 5.5 Flujo Completo de Integración Continua (Pipeline CI/CD)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. PROFESORES / BEDELÍA IFTS 2:                                             │
│    Publican en @ifts2de20 con hashtags temáticos:                           │
│    #IFTS2Practicas • #IFTS2Emprende • #IFTS2Masterclass • #IFTS2Eventos      │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                         (Cron programado cada 24 hs)
                                       │
┌──────────────────────────────────────▼──────────────────────────────────────┐
│ 2. GITHUB ACTIONS (`.github/workflows/instagram-sync.yml`):                 │
│    - Ejecuta `scripts/fetch_instagram.py`                                   │
│    - Consulta `graph.instagram.com/me/media`                                │
│    - Filtra posts por hashtags institucionales                              │
│    - Descarga y optimiza imágenes a `public/assets/instagram/`              │
│    - Genera `src/data/instagram-feed.json`                                  │
│    - Si el token supera los 30 días, lo refresca automáticamente            │
│    - Hace commit automático solo si hay nuevo contenido                     │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                         (Disparo de Webhook de Deploy)
                                       │
┌──────────────────────────────────────▼──────────────────────────────────────┐
│ 3. HOSTING ESTÁTICO (Cloudflare Pages / GitHub Pages - $0):                 │
│    - Recompila el sitio en Astro en < 30 segundos                            │
│    - Despliega HTML/CSS/JS estático puro sin servidor activo                │
│    - Rendimiento Lighthouse 100/100 • Sin base de datos que mantener        │
└─────────────────────────────────────────────────────────────────────────────┘
```
