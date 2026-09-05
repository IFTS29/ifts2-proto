# Sistema de Diseño y Arquitectura Web: IFTS N° 2
## Inspirado en el benchmark de Azafrán Escuela de Gastronomía

---

## 1. Diagnóstico y Benchmark (Azafrán Escuela vs. IFTS N° 2)

El análisis del sitio de **Azafrán Escuela de Gastronomía** (`azafranescuela.edu.ar/tecnico-superior-en-gastronomia/`) revela una estructura de alta conversión y claridad institucional:
- **Hero con credenciales oficiales inmediatas:** Título oficial, resolución ministerial, duración (3 años), modalidad y fechas clave.
- **Doble eje formativo:** Fuerte equilibrio entre la técnica culinaria y las materias duras (costos, administración, marketing, bromatología).
- **Prácticas Profesionalizantes destacadas:** Carga horaria anual explícita y convenios reales.
- **Grilla curricular navegable:** Desglose año por año entre materias anuales y cuatrimestrales.
- **Diferenciación de públicos:** Estudiantes actuales (Gestión Académica / Campus) vs. Aspirantes (Requisitos / Inscripción).

### Adaptación al IFTS N° 2 (Gestión Pública CABA)
El IFTS N° 2 tiene una ventaja competitiva única: **es educación superior estatal, pública y 100% gratuita**.
El eje central definido por Rectoría debe liderar la narrativa:
> *"No formamos chefs, formamos empresarios gastronómicos"*

---

## 2. Paleta de Colores y Tipografía

### Paleta Cromática
- **Base Principal (Dark Luxury / Culinario):** Slate 950 (`#090d16`) y Slate 900 (`#0f172a`). Aporta seriedad académica y estética gastronómica moderna.
- **Acento Primario (Saffron / Terracotta):** Amber 600 (`#d97706`) y Orange 700 (`#c2410c`). Evoca calidez, especias, gastronomía y dinamismo.
- **Identidad Institucional (Educación Pública CABA):** Emerald 700 (`#047857`) y Teal 800 (`#115e59`). Representa la formación técnica pública y validez nacional.
- **Superficies y Fondos:** Blanco puro (`#ffffff`) y Slate 50/100 (`#f8fafc`, `#f1f5f9`) para lectura descansada.
- **Bordes y Separadores:** Slate 200 (`#e2e8f0`).

### Tipografía
- **Títulos y Cabeceras:** `Oswald` o `Plus Jakarta Sans` (peso 700 / 800) en mayúsculas sobrias y tracking ajustado.
- **Cuerpo y Lectura:** `Plus Jakarta Sans` o `Inter` (peso 400, 500, 600) con altura de línea amplia (`leading-relaxed`) para programas de estudio y reglamentos.

---

## 3. Arquitectura de Información y Secciones de la Página

1. **Top Bar Institucional:** Dependencia de DGEST / Ministerio de Educación CABA, accesos a SIU Guaraní, Campus Moodle y Bedelía.
2. **Header de Navegación:** Logo IFTS 2, Carrera, Plan de Estudios, Prácticas Profesionalizantes, Comunidad Instagram, Horarios y Contacto.
3. **Hero Section:**
   - Eje: *"No formamos chefs, formamos empresarios gastronómicos"*.
   - Ficha técnica rápida: Duración 3 años | Título Oficial de Validez Nacional (Res. MEGC 1202/07) | Turno Vespertino | 100% Gratuito.
   - Botones de acción: *Plan de Estudios* y *Proceso de Ingreso*.
4. **Perfil del Egresado & Competencias:**
   - 4 pilares: Dirección de Cocinas, Gestión de Costos & Negocios, Seguridad Bromatológica, Emprendimientos y Eventos.
5. **Plan de Estudios Interactivo (Tabs por Año):**
   - 1° Año, 2° Año, 3° Año (anuales y cuatrimestrales).
   - Visualización clara del régimen de correlatividades y 160hs anuales de Prácticas Profesionalizantes.
6. **Sección Estrella: Carrusel de Comunidad & Prácticas en Vivo (Instagram @ifts2de20):**
   - **Ubicación:** Inmediatamente después del bloque de Prácticas Profesionalizantes y antes de la agenda académica.
   - **Formato:** Carrusel horizontal fluido con tarjetas de proporción fija uniforme (proporción 1:1 o 4:5 cuadrada/vertical de Instagram).
   - **Efecto Hover / Rollover:** Zoom sutil + degradé oscuro con resumen del post, fecha y tag temático.
   - **Lightbox / Modal:** Al hacer clic, abre el post completo con su copy y enlace a Instagram.
7. **Agenda Académica & Archivo Histórico (Solución al muro desordenado):**
   - Columna izquierda: Eventos vigentes del ciclo lectivo (Colación anual, Cierre de cuatrimestre).
   - Columna derecha: Acordeón de Archivo por Años (2025, 2024, 2023) para mantener la portada limpia.
8. **Bedelía & Trámites Frecuentes:**
   - Formulario de contacto directo a bedelía por mail + botones para constancias y programas.
9. **Footer Institucional:** Ubicación geográfica (D.E. 20, CABA), teléfonos, horarios de atención y enlaces ministeriales.

---

## 4. Arquitectura Profesional de Automatización de Instagram

Para responder a la solicitud de **automatización profesional** sin incurrir en costos de servidor ni sufrir tokens caídos, se define la siguiente arquitectura técnica:

```
┌─────────────────────────┐
│ Instagram @ifts2de20    │
│ (Nuevos Posts / Reels)  │
└────────────┬────────────┘
             │
             ▼ (Cada 12 horas o al publicar)
┌────────────────────────────────────────────────────────┐
│ GitHub Actions / Cloudflare Worker (Cron Job Gratis)   │
│ 1. Consulta Meta Graph API (Instagram Basic Display)   │
│ 2. Descarga imágenes a CDN/repo (evita links vencidos) │
│ 3. Genera el archivo optimizado: `instagram-feed.json` │
│ 4. Auto-renueva el token de 60 días en el día 45       │
└────────────┬───────────────────────────────────────────┘
             │
             ▼
┌────────────────────────────────────────────────────────┐
│ Sitio Web IFTS N° 2 (Astro / Next Estático)           │
│ Consume `instagram-feed.json` y renderiza el Carrusel │
│ Rendimiento: 100/100 Lighthouse • Costo de hosting: $0 │
└────────────────────────────────────────────────────────┘
```

### Componentes de la Solución Automatizada:
1. **Instagram Basic Display API (o Graph API para creadores):**
   - Endpoint: `GET https://graph.instagram.com/me/media?fields=id,caption,media_type,media_url,thumbnail_url,permalink,timestamp`
2. **Estrategia para evitar imágenes caídas (CDN Caching):**
   - Las URLs de medios de Instagram expiran después de 48-72 horas. La automatización descarga la imagen optimizada a WebP y la almacena en el repositorio o en Cloudflare R2/Images.
3. **Renovación automática del Token de Acceso (Long-Lived Token):**
   - El token de larga duración de Meta dura 60 días.
   - El script programado ejecuta automáticamente en el día 45:
     `GET https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token={TOKEN}`
   - Esto resetea los 60 días sin requerir intervención humana jamás.
4. **Filtro automático de etiquetas:**
   - La automatización lee los hashtags del copy (`#GuisoFest`, `#PracticasIFTS2`, `#Emprendedores`) y asigna automáticamente la categoría del carrusel.
