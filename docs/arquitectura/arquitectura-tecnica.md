# Arquitectura técnica — Prototipo sitio IFTS N°2 DE 20

Trabajo final tecnicatura IFTS-29. Este documento define el stack, el pipeline de contenido acordado y el sistema de automatización para la integración de Instagram.

---

## 1. Matriz de Decisión: Integración de Instagram (Costo $0)

| Criterio | Opción A: Embeds Manuales (iframes de Meta) | Opción B: Web Scraping no oficial | Opción C (Elegida): Instagram API with Instagram Login + CI/CD |
| :--- | :--- | :--- | :--- |
| **Nivel de Automatización** | Nulo (Manual: requiere pegar código post por post). | Alto, pero frágil (se rompe con cualquier cambio de HTML). | **Totalmente automatizado y desatendido.** |
| **Carga de Trabajo del IFTS** | Inviable (el equipo docente declaró no tener tiempo). | Nula. | **Mantenimiento CERO para el personal del IFTS.** |
| **Términos de Servicio (TOS)** | Aprobado. | Viola los términos de Meta (riesgo de baneo de IP). | **100% Oficial y en regla con Meta Developer TOS.** |
| **Estabilidad de Medios** | Alto impacto en performance (scripts pesados de terceros). | Alta tasa de fallo por bloqueo anti-bot. | **Imágenes cacheadas localmente: carga ultrarrápida.** |
| **Costo de Infraestructura** | $0 | $0 (hasta que bloquean IP y requiere proxies pagos). | **$0 / mes (Astro + GitHub Actions + Cloudflare Pages/GitHub Pages).** |

---

## 2. Stack general

| Capa | Elección | Por qué |
|---|---|---|
| Generador de sitio | **HTML/CSS/JS (Prototipo) -> Astro (Producción)** | Contenido mayormente estático (institucional, eventos) con islas de interactividad puntuales. Build rápido, sin servidor corriendo 24/7. |
| Contenido institucional / eventos | **Colecciones de contenido en Markdown** (`src/content/eventos/`) | Archivar = mover de carpeta por año. Sin base de datos que mantener. |
| Edición sin tocar código (opcional) | **Decap CMS** sobre el mismo repo | Le da a dirección una interfaz de edición sin depender de un desarrollador. |
| Hosting | **GitHub Pages** (o Cloudflare Pages) | Gratuito, cumple el requisito de "costos limitados" / "alojamiento gratuito". |
| Formulario de contacto → bedelía | Servicio externo gratuito (Formspree o Web3Forms) | Sin backend propio que mantener. |
| Sincronización de Instagram | **GitHub Actions** (cron diario) + **Instagram API with Instagram Login** | Automatiza la curaduría sin requerir App Review de Meta ni vincular una Página de Facebook. |

---

## 3. Pipeline de sincronización con Instagram

### 3.1 Requisitos previos (una sola vez)
1. La cuenta `@ifts2de20` debe ser cuenta **profesional** (Business o Creator).
2. Crear una app tipo *Business* en el Meta Developer Dashboard.
3. Agregar la cuenta del instituto como **tester** de esa app (Standard Access). Esto evita el proceso de App Review.
4. Generar un **token de larga duración** (Instagram User Access Token, ~60 días de vigencia) mediante el flujo de Login de Instagram (`graph.instagram.com`).
5. Guardar ese token como **secret** en el repositorio de GitHub.

*(Nota: La antigua Basic Display API fue discontinuada en Diciembre de 2024. El estándar actual es "Instagram API with Instagram Login").*

### 3.2 Job programado (GitHub Action, cron diario)

**Paso 1 — Traer los posts recientes**
```http
GET https://graph.instagram.com/me/media?fields=id,caption,media_type,media_url,permalink,timestamp&access_token={TOKEN}
```
*Consumo de cuota: 1 a 2 llamadas diarias (0.04% del límite oficial).*

**Paso 2 — Clasificar por hashtag**
El script recorre el `caption` de cada post y busca hashtags de categoría predefinidos (`#eventos`, `#cocina`, `#institucional`). Si el caption no tiene ninguno, el post se descarta automáticamente.

**Paso 3 — Descargar la imagen y evitar el link roto**
Las URLs de imágenes (`media_url`) expiran tras 48 a 72 horas por razones de seguridad de Meta. Para evitar esto:
- Se descarga el archivo binario desde `media_url`.
- Se guarda localmente (ej. en `public/assets/instagram/`).
- La web sirve sus propias imágenes locales con disponibilidad permanente del 100%.

**Paso 4 — Commit + trigger de build**
El Action commitea los archivos nuevos al repo (`src/data/instagram-feed.json` e imágenes). Ese commit dispara automáticamente el build estático.

**Paso 5 — Refresco desatendido del token**
El token de larga duración vence a los 60 días. Cada vez que el Action corre y detecta que el token tiene más de 30 días, llama al endpoint de refresco y actualiza el secret del repositorio vía GitHub API, logrando un ciclo perpetuo.
```http
GET https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token={LONG_LIVED_TOKEN}
```

### 3.3 Diagrama de flujo (resumen)

```
[Instagram @ifts2de20]
        |  (post nuevo con #eventos, #cocina, etc.)
        v
[GitHub Action - cron diario]
   1. GET /me/media (Instagram API with Instagram Login)
   2. Filtra posts nuevos por hashtag de categoría
   3. Descarga imagen -> public/assets/instagram/
   4. Actualiza data JSON
   5. Evalúa y refresca token de Meta si es necesario
   6. Commit al repo
        |
        v
[GitHub Pages / Cloudflare Pages] --(rebuild automático)--> [Sitio publicado]
```

---

## 4. Estructura de contenido propuesta

```
src/content/
  institucional/       -> estático: plan de carrera, perfil del egresado, correlatividades, autoridades
  academico/            -> semi-dinámico: horarios vigentes, materias por cuatrimestre, trámites
  eventos/
    2026/               -> eventos del año en curso
    archivo/            -> años anteriores
  novedades/            -> posts de Instagram sincronizados (categoría #institucional, etc.)
```

---

## 5. Costos y mantenimiento (resumen)

| Ítem | Costo | Mantenimiento requerido |
|---|---|---|
| Hosting | $0 | Ninguno |
| GitHub Actions (cron) | $0 (dentro del free tier) | Ninguno |
| Sincronización Instagram | $0 | Ninguno (el script auto-renueva el token) |
| Formulario de contacto | $0 | Ninguno |
