import re

with open("c:\\Users\\marth\\OneDrive\\Documents\\Tzutujil2\\gramatica.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace <style> to </style> with <link rel="stylesheet" href="styles.css">
# and replace Playfair link with Lora
content = re.sub(
    r'<link href="[^"]*Playfair\+Display[^"]*" rel="stylesheet">\s*<style>.*?</style>',
    '<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Source+Serif+4:ital,wght@0,300;0,400;0,600;1,300&display=swap" rel="stylesheet">\n  <link rel="stylesheet" href="styles.css">',
    content,
    flags=re.DOTALL
)

# Replace <header> to </header> with unified header
new_header = """  <!-- TOP BAR -->
  <div class="top-bar">
    <div class="social-icons">
      <a href="https://www.instagram.com/idiomatzutujil/" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
        <img src="assets/img/instagram.svg" alt="Instagram">
      </a>
      <a href="https://www.facebook.com/profile.php?id=100065151015711" target="_blank" rel="noopener noreferrer" aria-label="Facebook">
        <img src="assets/img/facebook.svg" alt="Facebook">
      </a>
    </div>
    <div class="logo">Idioma maya Tz'utujil</div>
    <a class="subscribe-button" href="https://wa.me/50244725900" target="_blank" rel="noopener noreferrer">Clases Online</a>
  </div>

  <!-- NAVBAR -->
  <nav class="navbar" id="navbar" role="navigation" aria-label="Navegación principal">
    <div class="logo">Idioma <span>Tz'utujil</span></div>
    <ul class="nav-links">
      <li><a href="index.html">Inicio</a></li>
      <li><a href="tienda.html">Tienda</a></li>
      <li><a href="gramatica.html" class="activo-nav">Idioma</a></li>
      <li><a href="cultura.html">Cultura</a></li>
    </ul>
    <button class="hamburger" onclick="toggleMenu()" aria-label="Abrir menú" aria-expanded="false" id="hamburger-btn">☰</button>
  </nav>

  <!-- MOBILE MENU -->
  <nav class="nav-mobile" id="nav-mobile" aria-label="Menú móvil">
    <a href="index.html">Inicio</a>
    <a href="tienda.html">Tienda</a>
    <a href="gramatica.html">Idioma</a>
    <a href="cultura.html">Cultura</a>
    <a href="https://wa.me/50244725900" target="_blank" class="mobile-cta">Clases aqui</a>
  </nav>"""

content = re.sub(
    r'<header>.*?</header>',
    new_header,
    content,
    flags=re.DOTALL
)

new_footer = """  <!-- FOOTER -->
  <footer>
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="logo-footer">Idioma Maya <span>Tz'utujil</span></div>
        <p>Preservando el idioma maya Tz'utujil a través de la educación, los materiales didácticos y el orgullo cultural. Desde las orillas del Lago Atitlán para el mundo.</p>
      </div>
      <div class="footer-col">
        <h4>Páginas</h4>
        <ul>
          <li><a href="index.html">Inicio</a></li>
          <li><a href="tienda.html">Tienda</a></li>
          <li><a href="gramatica.html">Idioma</a></li>
          <li><a href="cultura.html">Cultura</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Redes sociales</h4>
        <ul>
          <li><a href="https://www.facebook.com/profile.php?id=100065151015711" target="_blank" rel="noopener noreferrer">Facebook</a></li>
          <li><a href="https://www.instagram.com/idiomatzutujil/" target="_blank" rel="noopener noreferrer">Instagram</a></li>
          <li><a href="https://wa.me/50244725900" target="_blank" rel="noopener noreferrer">WhatsApp</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© <span id="anio-actual"></span> Idioma maya Tz'utujil. Todos los derechos reservados.</p>
      <span class="footer-tz">"Chi ya' kanoq qa'iij" </span>
    </div>
  </footer>"""

content = re.sub(
    r'<footer>.*?</footer>',
    new_footer,
    content,
    flags=re.DOTALL
)

with open("c:\\Users\\marth\\OneDrive\\Documents\\Tzutujil2\\gramatica.html", "w", encoding="utf-8") as f:
    f.write(content)
    
css_to_append = """
/* ── GRAMMATICA ALIASES ── */
:root {
  --tierra: var(--verde);
  --jade: var(--verde-osc);
  --jade-claro: var(--verde-med);
  --jade-suave: var(--verde-claro);
  --ocre: var(--dorado);
  --ocre-claro: var(--dorado-lt);
  --humo: var(--crema);
  --carbon: var(--texto);
  --gris-medio: var(--texto-mid);
}

/* ── PAGE SUB-TABS ── */
.page-tabs { background: var(--blanco); border-bottom: 2px solid var(--jade-suave); display: flex; gap: 0; overflow-x: auto; padding: 0 2rem; }
.page-tabs a { text-decoration: none; color: var(--gris-medio); font-size: 0.88rem; font-family: 'Source Serif 4', serif; padding: 0.85rem 1.3rem; border-bottom: 3px solid transparent; white-space: nowrap; transition: all 0.2s; }
.page-tabs a:hover { color: var(--jade); border-bottom-color: var(--jade-claro); }
.page-tabs a.activo { color: var(--jade); border-bottom-color: var(--jade); font-weight: 600; }

.section-subtitle { color: var(--gris-medio); font-size: 0.92rem; margin-bottom: 1.8rem; font-style: italic; }

/* ══════════════════════════════════
   SECCIÓN 1: CURSOS
══════════════════════════════════ */
#cursos { margin-bottom: 4rem; }
.cursos-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 1.5rem; }
.curso-card { background: var(--blanco); border-radius: var(--radio); overflow: hidden; border: 1px solid var(--borde); transition: transform 0.25s, box-shadow 0.25s; display: flex; flex-direction: column; }
.curso-card:hover { transform: translateY(-4px); box-shadow: 0 12px 30px rgba(0,0,0,0.12); }
.curso-banner { padding: 1.4rem 1.6rem 1rem; position: relative; }
.curso-card.nativos .curso-banner { background: linear-gradient(135deg, #4e9b8b, #fbe27f); }
.curso-card.maestros .curso-banner { background: linear-gradient(135deg, #4e9b8b, #db8055); }
.curso-card.extranjeros .curso-banner { background: linear-gradient(135deg, #fbe27f, #4e9b8b); }
.curso-icono { font-size: 2.2rem; margin-bottom: 0.6rem; display: block; }
.curso-banner h3 { font-family: 'Lora', serif; font-size: 1.2rem; color: var(--blanco); margin-bottom: 0.2rem; }
.curso-banner p { color: rgba(255,255,255,0.75); font-size: 0.82rem; font-style: italic; }
.nivel-badge { position: absolute; top: 1rem; right: 1rem; background: rgba(255,255,255,0.2); color: var(--blanco); font-size: 0.7rem; padding: 0.2rem 0.6rem; border-radius: 20px; border: 1px solid rgba(255,255,255,0.35); letter-spacing: 0.08em; }
.curso-body { padding: 1.3rem 1.6rem; flex: 1; display: flex; flex-direction: column; }
.curso-body ul { list-style: none; margin-bottom: 1.2rem; flex: 1; }
.curso-body ul li { font-size: 0.88rem; color: var(--gris-medio); padding: 0.3rem 0; padding-left: 1.2rem; position: relative; }
.curso-body ul li::before { content: '›'; position: absolute; left: 0; color: var(--jade-claro); font-weight: bold; }
.btn-curso { display: inline-block; text-align: center; text-decoration: none; padding: 0.6rem 1.2rem; border-radius: 6px; font-size: 0.85rem; font-family: 'Source Serif 4', serif; transition: all 0.2s; border: 2px solid; }
.curso-card.nativos .btn-curso { color: var(--jade); border-color: var(--jade); }
.curso-card.nativos .btn-curso:hover { background: var(--jade); color: var(--blanco); }
.curso-card.maestros .btn-curso { color: var(--tierra); border-color: var(--tierra); }
.curso-card.maestros .btn-curso:hover { background: var(--tierra); color: var(--blanco); }
.curso-card.extranjeros .btn-curso { color: var(--jade); border-color: var(--jade); }
.curso-card.extranjeros .btn-curso:hover { background: var(--jade); color: var(--blanco); }

/* ══════════════════════════════════
   SECCIÓN 2: PRACTICE SPEAKING (Audios y Ejercicios)
══════════════════════════════════ */
#practica { margin-bottom: 4rem; }
.practica-layout { display: grid; grid-template-columns: 1fr 1fr; gap: 1.8rem; }
@media (max-width: 700px) { .practica-layout { grid-template-columns: 1fr; } }
.consonantes-panel { background: var(--blanco); border-radius: var(--radio); border: 1px solid var(--borde); overflow: hidden; }
.panel-header { background: var(--jade); padding: 1rem 1.4rem; color: var(--blanco); font-family: 'Lora', serif; font-size: 1rem; }
.panel-header small { display: block; font-family: 'Source Serif 4', serif; font-size: 0.78rem; opacity: 0.8; font-style: italic; margin-top: 0.1rem; }
.consonante-fila { display: flex; align-items: center; gap: 0.8rem; padding: 0.9rem 1.4rem; border-bottom: 1px solid var(--jade-suave); }
.consonante-fila:last-child { border-bottom: none; }
.consonante-simbolo { font-family: 'Lora', serif; font-size: 1.4rem; color: var(--jade); font-weight: 700; width: 36px; }
.audio-btns { display: flex; flex-wrap: wrap; gap: 5px; flex: 1; }
.audio-btn { padding: 4px 10px; font-size: 0.8rem; cursor: pointer; background: var(--jade-suave); border: 1px solid #b7e4c7; border-radius: 4px; font-family: 'Source Serif 4', serif; transition: all 0.15s; color: var(--jade); }
.audio-btn:hover { background: var(--jade-claro); color: var(--blanco); border-color: var(--jade-claro); }
.audio-btn.playing { background: var(--jade); color: var(--blanco); }
.dialogo-panel { display: flex; flex-direction: column; gap: 1.2rem; }
details { background: var(--blanco); border: 1px solid var(--borde); border-radius: var(--radio); overflow: hidden; }
summary { padding: 1rem 1.4rem; cursor: pointer; font-weight: 600; font-size: 0.92rem; color: var(--tierra); user-select: none; list-style: none; display: flex; align-items: center; justify-content: space-between; }
summary::after { content: '▾'; color: var(--ocre); font-size: 1rem; }
details[open] summary::after { content: '▴'; }
details[open] summary { border-bottom: 1px solid var(--jade-suave); }
.details-body { padding: 1.2rem 1.4rem; }
.dialogo-texto { font-size: 0.9rem; line-height: 1.9; background: var(--ocre-claro); border-left: 3px solid var(--ocre); padding: 0.8rem 1rem; border-radius: 0 6px 6px 0; }
.dialogo-texto .hablante { font-weight: 600; color: var(--tierra); }
audio { width: 100%; margin-top: 0.5rem; accent-color: var(--jade); }
.ejercicio-pregunta { font-size: 0.9rem; margin-bottom: 1rem; color: var(--carbon); }
.opciones { list-style: none; display: flex; flex-direction: column; gap: 0.5rem; }
.opcion-btn { width: 100%; text-align: left; padding: 0.7rem 1rem; background: var(--humo); border: 1.5px solid var(--borde); border-radius: 6px; cursor: pointer; font-family: 'Source Serif 4', serif; font-size: 0.88rem; transition: all 0.15s; color: var(--carbon); }
.opcion-btn:hover { border-color: var(--jade-claro); background: var(--jade-suave); }
.opcion-btn.correcta { background: #d8f3dc; border-color: var(--jade); color: var(--jade); }
.opcion-btn.incorrecta { background: #ffe0e0; border-color: #e07070; color: #db8055; }
.feedback-ej { margin-top: 0.8rem; font-size: 0.85rem; font-style: italic; display: none; }

/* ══════════════════════════════════
   SECCIÓN 3: TEMAS POPULARES
══════════════════════════════════ */
#temas { margin-bottom: 4rem; }
.temas-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(230px, 1fr)); gap: 1.2rem; }
.tema-card { background: var(--blanco); border: 1px solid var(--borde); border-radius: var(--radio); padding: 1.3rem 1.4rem; text-decoration: none; color: inherit; display: flex; gap: 1rem; align-items: flex-start; transition: all 0.2s; position: relative; overflow: hidden; }
.tema-card::before { content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 4px; }
.tema-card.tienda::before { background: var(--ocre); }
.tema-card.gramatica::before { background: var(--jade); }
.tema-card:hover { transform: translateX(4px); box-shadow: 0 4px 16px rgba(0,0,0,0.09); }
.tema-emoji { font-size: 1.6rem; flex-shrink: 0; margin-top: 0.1rem; }
.tema-info { flex: 1; }
.tema-info h4 { font-family: 'Lora', serif; font-size: 0.98rem; color: var(--carbon); margin-bottom: 0.25rem; line-height: 1.3; }
.tema-info p { font-size: 0.78rem; color: var(--gris-medio); font-style: italic; }
.tema-badge { font-size: 0.68rem; padding: 0.15rem 0.5rem; border-radius: 20px; margin-top: 0.4rem; display: inline-block; }
.tema-card.tienda .tema-badge { background: var(--ocre-claro); color: #7a5a10; }
.tema-card.gramatica .tema-badge { background: var(--jade-suave); color: var(--jade); }
.temas-ver-mas { text-align: center; margin-top: 1.5rem; }
.btn-ver-mas { display: inline-block; text-decoration: none; color: var(--jade); border: 1.5px solid var(--jade); padding: 0.6rem 1.5rem; border-radius: 25px; font-size: 0.88rem; transition: all 0.2s; }
.btn-ver-mas:hover { background: var(--jade); color: var(--blanco); }

@media (max-width: 600px) {
  .cursos-grid { grid-template-columns: 1fr; }
}
"""

with open("c:\\Users\\marth\\OneDrive\\Documents\\Tzutujil2\\styles.css", "a", encoding="utf-8") as f:
    f.write(css_to_append)
