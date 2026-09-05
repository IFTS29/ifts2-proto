# Arquitectura técnica — Prototipo sitio IFTS N°2 DE 20

Trabajo final tecnicatura IFTS-29. Este documento complementa a `relevamiento-refactor-ifts2.md` y define el stack y el pipeline de contenido acordados.

---

## 1. Stack general

| Capa | Elección | Por qué |
|---|---|---|
| Generador de sitio | **Astro** | Contenido mayormente estático (institucional, eventos) con islas de interactividad puntuales (rollover, carrusel de Instagram). Build rápido, sin servidor corriendo 24/7. |
| Contenido institucional / eventos | **Colecciones de contenido en Markdown** (`src/content/eventos/`, `src/content/institucional/`) | Archivar = mover de carpeta por año. Sin base de datos que mantener. |
| Edición sin tocar código (opcional, fase 2) | **Decap CMS** sobre el mismo repo | Le da a Cecilia/María una interfaz de edición sin depender de un desarrollador para cambios chicos. |
| Hosting | **Cloudflare Pages** (o GitHub Pages / Netlify) | Gratuito, cumple el requisito de "costos limitados" / "alojamiento gratuito". |
| Formulario de contacto → bedelía | Servicio externo gratuito (Formspree o Web3Forms) | Sin backend propio que mantener. |
| Sincronización de Instagram | **GitHub Actions** (cron diario) + **Instagram API with Instagram Login** | Automatiza la curaduría sin requerir App Review de Meta ni vincular una Página de Facebook. |

---

## 2. Pipeline de sincronización con Instagram

### 2.1 Requisitos previos (una sola vez)
1. La cuenta `@ifts2de20` debe ser cuenta **profesional** (Business o Creator) — ya lo es o se convierte gratis desde la config de Instagram.
2. Crear una app tipo *Business* en el Meta Developer Dashboard.
3. Agregar la cuenta del instituto como **tester** de esa app (Standard Access). Esto evita el proceso de App Review, porque no se sirven cuentas de terceros — solo la propia.
4. Generar un **token de larga duración** (Instagram User Access Token, ~60 días de vigencia) mediante el flujo de Login de Instagram (`graph.instagram.com`).
5. Guardar ese token como **secret** en el repositorio de GitHub (no en el código).

### 2.2 Job programado (GitHub Action, cron diario)

**Paso 1 — Traer los posts recientes**
```
GET https://graph.instagram.com/me/media
    ?fields=id,caption,media_type,media_url,permalink,timestamp
    &access_token={TOKEN}
```

Campos solicitados y para qué sirve cada uno:

| Campo | Uso |
|---|---|
| `id` | Identificador único, para no duplicar posts ya procesados |
| `caption` | Texto del post — de acá se extraen los hashtags de clasificación |
| `media_type` | IMAGE / VIDEO / CAROUSEL_ALBUM — para renderizar distinto según tipo |
| `media_url` | URL temporal (expira en 48-72hs) — se descarga la imagen y se descarta esta URL |
| `permalink` | Link permanente al post original en Instagram (para el botón "ver en Instagram") |
| `timestamp` | Fecha de publicación — para ordenar y archivar por año |

**Paso 2 — Clasificar por hashtag**
El script recorre el `caption` de cada post y busca hashtags de categoría predefinidos:

```
CATEGORIAS = {
  "#eventos": "eventos",
  "#cocina": "academico",
  "#institucional": "institucional",
}
```

Si el caption no tiene ninguno de estos hashtags, el post se descarta (esto es lo que reemplaza la curaduría manual: el community manager decide qué se publica en la web con el hashtag que usa al postear en Instagram).

**Paso 3 — Descargar la imagen y evitar el link roto**
Por cada post nuevo que matchea una categoría:
- Descargar el archivo desde `media_url`.
- Guardarlo en `public/instagram/{id}.jpg` (o subirlo a un bucket si el repo crece mucho).
- Nunca guardar `media_url` en el contenido final — solo la ruta local.

**Paso 4 — Escribir el archivo de contenido**
Se genera un archivo Markdown/JSON por post nuevo dentro de la colección correspondiente, por ejemplo:

```
src/content/eventos/2026/{id}.md
---
title: "Extraído del caption"
fecha: 2026-09-04
imagen: /instagram/{id}.jpg
permalink: https://instagram.com/p/xxxx
fuente: instagram
---
```

**Paso 5 — Commit + trigger de build**
El Action commitea los archivos nuevos al repo. Ese commit dispara automáticamente el build en Cloudflare Pages.

**Paso 6 — Refresco de token**
Antes de que venza (60 días), el mismo Action —corriendo cada pocos días— llama al endpoint de refresh de token y actualiza el secret del repo. Es la única tarea de mantenimiento periódico real de todo el pipeline.

### 2.3 Diagrama de flujo (resumen)

```
[Instagram @ifts2de20]
        |  (post nuevo con #eventos, #cocina, etc.)
        v
[GitHub Action - cron diario]
   1. GET /me/media (Instagram API with Instagram Login)
   2. Filtra posts nuevos por hashtag de categoría
   3. Descarga imagen -> public/instagram/
   4. Escribe archivo de contenido -> src/content/{categoria}/
   5. Commit al repo
        |
        v
[Cloudflare Pages] --(rebuild automático)--> [Sitio publicado]
```

### 2.4 Qué NO se usa (y por qué)
- **Hashtag Search API (Meta)**: solo sirve para buscar contenido de terceros, requiere App Review empresarial y limita a 30 hashtags/semana. No aplica porque acá se lee el feed propio, no se busca contenido ajeno.
- **Instagram Basic Display API**: discontinuada por Meta en diciembre 2024.
- **Facebook Login para Instagram**: requiere vincular una Página de Facebook; la ruta "Instagram Login" evita ese paso extra.

---

## 3. Estructura de contenido propuesta

```
src/content/
  institucional/       -> estático: plan de carrera, perfil del egresado, correlatividades, autoridades
  academico/            -> semi-dinámico: horarios vigentes, materias por cuatrimestre, trámites
  eventos/
    2026/               -> eventos del año en curso
    archivo/
      2025/
      2024/
      ...
  novedades/            -> posts de Instagram sincronizados (categoría #institucional, etc.)
```

Archivar un evento = mover su carpeta de `eventos/2026/` a `eventos/archivo/2026/` al cerrar el año — sin tocar código ni base de datos.

---

## 4. Costos y mantenimiento (resumen)

| Ítem | Costo | Mantenimiento requerido |
|---|---|---|
| Hosting (Cloudflare Pages) | $0 | Ninguno |
| GitHub Actions (cron) | $0 (dentro del free tier) | Ninguno |
| Sincronización Instagram | $0 | Refrescar token cada ~60 días (automatizable) |
| Formulario de contacto | $0 (plan free de Formspree/Web3Forms) | Ninguno |
| CMS de edición (Decap, fase 2) | $0 | Ninguno |

---

## 5. Pendientes para el prototipo
- Definir la lista final de hashtags de categoría con el community manager del IFTS (`#eventos`, `#cocina`, etc.).
- Decidir si Decap CMS se incluye en el prototipo o queda para una fase posterior.
- Migrar el contenido institucional actual (PDFs del sitio viejo) a las colecciones Markdown.
