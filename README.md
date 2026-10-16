# Renovación web del IFTS N.° 2

Sitio institucional del IFTS N.° 2 (D.E. 20) y su panel de administración. Lo desarrolla el equipo 404-Solutions (IFTS N.° 29) como proyecto integrador de Práctica Profesionalizante IV, para reemplazar el Google Site actual del instituto.

Este repositorio junta dos trabajos que se hicieron por separado:

- El **prototipo del sitio y del panel** (HTML, CSS y JavaScript), que es lo que se ve en pantalla.
- La **documentación de arquitectura y el pipeline de Instagram** (script de Python y GitHub Actions).

## Estado actual

El sitio es un prototipo navegable: no tiene backend ni base de datos. Los formularios, el login y el panel simulan sus respuestas y nada se guarda al recargar. Las publicaciones de Instagram que se muestran son de ejemplo.

Falta para la Etapa 3: el backend con su base de datos, la autenticación real, la integración con Instagram con datos reales y las pruebas.

## Cómo verlo

1. Clonar el repositorio y abrir la carpeta en VS Code.
2. Abrir `index.html` con la extensión Live Server (clic derecho, "Open with Live Server"). También se puede abrir directamente en el navegador.

No hace falta instalar nada. Para recorrer todas las pantallas está el botón "Pantallas del prototipo", abajo a la derecha.

## Estructura

```
index.html              Todas las pantallas (sitio público y panel), cada una en un <div data-pagina="...">
css/styles.css          Estilos
js/app.js               Navegación por rutas (#/inicio, #/admin...), roles, login, descargas y usuarios simulados
js/imagenes.js          Lista de imágenes que usa el sitio (apuntan a img/)
js/main.js              Del primer prototipo; el sitio actual ya no lo usa
img/                    Imágenes
docs/                   Documentación (ver abajo) y la guía de preingreso en PDF
data/                   Feed de Instagram generado por el script
scripts/                fetch_instagram.py: trae las publicaciones de Instagram
.github/workflows/      instagram-sync.yml: ejecuta el script todos los días
```

Las pantallas se cambian con el hash de la URL (por ejemplo `#/eventos` o `#/admin-usuarios`).

## Pantallas

Sitio público: inicio, la carrera, ingreso, alumnos, eventos, detalle de un evento y contacto.

Panel de administración: inicio de sesión, inicio del panel, eventos, cargar un evento, información académica, contenido institucional y usuarios.

El acceso al panel no está en el menú superior: está en el pie de página ("Acceso institucional") y en la ruta `#/login`.

## Documentación

- `docs/arquitectura/arquitectura-tecnica.md`: stack propuesto y pipeline de sincronización con Instagram.
- `docs/diseno/sistema-de-diseno.md`: lineamientos de diseño del primer prototipo.
- `docs/relevamiento/`: notas de reuniones y material de articulación entre el IFTS 2 y el IFTS 29.

## Instagram

El script `scripts/fetch_instagram.py` usa la API de Instagram con Instagram Login para traer las publicaciones de la cuenta institucional, y el workflow `.github/workflows/instagram-sync.yml` lo ejecuta una vez por día. Hoy genera datos de ejemplo (`mock_1` a `mock_3`) porque todavía no está cargado el token de la cuenta real.

Para activarlo con datos reales falta que el instituto comparta la clave de acceso de la cuenta (que ya es profesional) y acepte la invitación de solo lectura. Antes de eso, la integración se va a probar con una cuenta de prueba.

Cosas a corregir en este pipeline:

- El nombre de la cuenta aparece de dos formas (`@ifts_2_ok` en el sitio y `@ifts2de20` en el workflow).
- El script clasifica por hashtags como `#eventos` o `#cocina`, y el hashtag acordado con el cliente es `#IFTSEventos`.
- Las imágenes se guardan en `public/assets/instagram/`, una carpeta que este repo no tiene, y el sitio todavía apunta a imágenes externas.
- El workflow no guarda en el secret el token renovado.

## Cambios de la 2.ª reunión con el instituto (7/10/2026)

Salen del acta de la reunión.

### Hechos en el prototipo (simulados)

- **Acceso oculto.** El login se sacó del menú superior. Tiene un límite de 5 intentos fallidos (después se bloquea 15 minutos) y pide contraseñas de 8 o más caracteres.
- **Dos roles.** Administrador, con acceso total, y Bedelía, que solo ve Información académica. Si Bedelía intenta entrar a otra pantalla escribiendo la ruta, vuelve al inicio del panel. En el login, un correo que empieza con "bedel" entra como Bedelía; el resto, como administrador. Desde el menú de pantallas se puede ver cada rol.
- **Gestión de usuarios.** Pantalla nueva, solo para administradores: alta con rol, validación de campos vacíos, de correo repetido y de contraseña (8 o más caracteres, con letras y números), y baja con confirmación. La lista es de ejemplo; el instituto va a completar los datos de las cuentas.
- **Descarga de eventos archivados.** En Eventos hay una barra para descargar por año, por cuatrimestre o por evento, y un botón en cada evento archivado. Por ahora solo muestra el aviso de que se preparó la descarga.

### Pendientes: dependen de una respuesta del instituto

- **Archivo en el sitio público.** Falta saber si los eventos de años anteriores se ven en el sitio o solo en el panel.
- **Aprobación previa de Instagram.** Falta saber si la quieren. Si no, se saca la pestaña "Para revisar", los botones Aprobar y Descartar y el indicador de publicaciones para revisar.
- **Ingreso y cuatrimestre.** Hoy el ingreso figura como 2027. Faltan los datos reales y saber si hay ingreso a mitad de año.
- **Autoridades.** Hoy figuran la rectora y la tutora. Falta saber si se suman la secretaría académica o el asesor pedagógico.
- **Plan de estudios.** Falta el PDF del régimen de correlatividades, si lo tienen, y la información de cada materia.

### Pendientes: trabajo del equipo

- **Formulario de contacto por motivo.** El formulario ya tiene el campo "Motivo de la consulta". Falta derivar cada motivo a un correo distinto (Bedelía, institucional, tutoría). El plan gratuito de los servicios de formularios admite un solo destino por formulario, así que hay que investigar la alternativa.
- **Más de una carrera.** El menú y las secciones "La carrera" y "Plan de estudios" asumen una sola. Hay que preparar la estructura para sumar otras.
- **Detalle de la vista mobile del panel.** Menor. Miguel ya lo había corregido en Figma.

### Compromisos abiertos de la reunión

- El instituto completa los datos de las cuentas: tres con acceso total y dos de Bedelía.
- El instituto comparte la clave de Instagram y acepta la invitación de solo lectura.
- Raquel prueba la integración con una cuenta de Instagram de prueba antes de usar la del instituto.
- Valeria investiga si N8N sirve para automatizar Instagram con el sitio.
- El equipo investiga qué pasa cuando una publicación no lleva el hashtag.

### Preguntas que no se le hicieron al instituto

- Videos: si prefieren subirlos o dejarlos como enlace a Instagram.
- Dominio .edu.ar y qué pasa con el Google Site durante la transición.
- Si el teléfono y el correo institucional del sitio actual siguen vigentes.
- Enlaces de preinscripción y de Mi Argentina.
- Si tienen fotos oficiales (el prototipo usa las del sitio actual y algunas generadas con IA).
- Nombre exacto de la cuenta de Instagram y hashtag definitivo.

## Equipo

404-Solutions, IFTS N.° 29: Miguel Angel Flores Meehan, Valeria Thomas, Mario David González Benítez, Mariana Aiello y Raquel Rodriguez Herlein.
