/**
 * Lógica de interacción para el portal IFTS N° 2
 * - Datos simulados de Instagram
 * - Navegación del Plan de Estudios
 * - Controles y filtros del Carrusel de Instagram
 * - Modal / Lightbox accesible para publicaciones
 */

// 1. Datos simulados del feed institucional de Instagram (@ifts_2_ok)
const postsData = {
  1: {
    tag: "Eventos & Concursos",
    date: "02 Septiembre 2026",
    title: "Concurso Anual de Guisos Criollos",
    desc: "Los estudiantes de 2° año compitieron en la recreación de recetas tradicionales argentinas calculando costos reales de producción, mermas y rendimiento por porción bajo la supervisión de la brigada docente.",
    img: "https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=1000&q=80"
  },
  2: {
    tag: "Emprendimientos",
    date: "28 Agosto 2026",
    title: "Caso de Éxito: Bakery & Café de Graduados",
    desc: "Felicitamos a los egresados de la promoción 2024 que abrieron su propio local comercial en Caballito, validando su modelo de negocio desarrollado en el proyecto final de la carrera.",
    img: "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=1000&q=80"
  },
  3: {
    tag: "Masterclass",
    date: "19 Agosto 2026",
    title: "Masterclass: Chocolatería & Templado",
    desc: "Taller especial práctico enfocado en el templado por siembra, emulsiones y la ingeniería de precios para bombonería fina artesanal.",
    img: "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=1000&q=80"
  },
  4: {
    tag: "Prácticas en Cocina",
    date: "12 Agosto 2026",
    title: "Despacho de Cocina y Tiempos de Salón",
    desc: "Simulacro de servicio real: cómo coordinar la brigada de comandas en tiempo real asegurando la inocuidad bromatológica según normas HACCP.",
    img: "https://images.unsplash.com/photo-1577219491135-ce391730fb2c?auto=format&fit=crop&w=1000&q=80"
  },
  5: {
    tag: "Masterclass",
    date: "05 Agosto 2026",
    title: "Taller de Enología & Cartas de Vinos",
    desc: "Análisis sensorial de varietales representativos del país y estructuración de cartas de bebidas orientadas al ticket promedio del establecimiento gastronómico.",
    img: "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?auto=format&fit=crop&w=1000&q=80"
  }
};

// 2. Control de Pestañas del Plan de Estudios
function switchYear(year) {
  ['year1', 'year2', 'year3'].forEach(y => {
    const tab = document.getElementById(`tab-${y}`);
    const content = document.getElementById(`content-${y}`);
    if (tab && content) {
      if (y === year) {
        tab.classList.remove('text-slate-600');
        tab.classList.add('bg-blue-900', 'text-white');
        content.classList.remove('hidden');
      } else {
        tab.classList.remove('bg-blue-900', 'text-white');
        tab.classList.add('text-slate-600');
        content.classList.add('hidden');
      }
    }
  });
}

// 3. Control de desplazamiento del Carrusel de Instagram
function scrollCarousel(direction) {
  const carousel = document.getElementById('instagram-carousel');
  if (!carousel) return;
  const cardWidth = 320; // Ancho base de tarjeta + gap
  carousel.scrollBy({
    left: direction * cardWidth,
    behavior: 'smooth'
  });
}

// 4. Filtros de categoría del Carrusel
function filterFeed(category) {
  const items = document.querySelectorAll('.feed-item');
  const buttons = ['all', 'emprendimientos', 'masterclass', 'cocina', 'eventos'];

  buttons.forEach(b => {
    const btn = document.getElementById(`btn-filter-${b}`);
    if (btn) {
      if (b === category) {
        btn.classList.remove('bg-slate-100', 'text-slate-700');
        btn.classList.add('bg-blue-900', 'text-white');
      } else {
        btn.classList.remove('bg-blue-900', 'text-white');
        btn.classList.add('bg-slate-100', 'text-slate-700');
      }
    }
  });

  items.forEach(item => {
    if (category === 'all' || item.getAttribute('data-category') === category) {
      item.style.display = 'block';
    } else {
      item.style.display = 'none';
    }
  });
}

// 5. Modal / Lightbox accesible de publicaciones
function openPostModal(id) {
  const post = postsData[id];
  if (!post) return;

  const modalImg = document.getElementById('modal-img');
  const modalTag = document.getElementById('modal-tag');
  const modalDate = document.getElementById('modal-date');
  const modalTitle = document.getElementById('modal-title');
  const modalDesc = document.getElementById('modal-desc');
  const modal = document.getElementById('post-modal');

  if (modalImg) modalImg.src = post.img;
  if (modalTag) modalTag.innerText = post.tag;
  if (modalDate) modalDate.innerText = post.date;
  if (modalTitle) modalTitle.innerText = post.title;
  if (modalDesc) modalDesc.innerText = post.desc;

  if (modal) {
    modal.classList.remove('hidden');
    modal.classList.add('flex');
    document.body.style.overflow = 'hidden'; // Evita scroll de fondo
  }
}

function closePostModal(e) {
  if (e.target.id === 'post-modal') {
    closePostModalDirect();
  }
}

function closePostModalDirect() {
  const modal = document.getElementById('post-modal');
  if (modal) {
    modal.classList.remove('flex');
    modal.classList.add('hidden');
    document.body.style.overflow = ''; // Restaura scroll
  }
}

// Cerrar modal al presionar tecla Escape
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    closePostModalDirect();
  }
});
