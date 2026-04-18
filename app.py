import streamlit as st
import base64
from img_data import IMG_LOGO, IMG_DESTAQUE, IMG_ELETRICA, IMG_HIDRAULICA, IMG_DICAS, IMG_INFORMACOES

def show_img(b64_string, **kwargs):
    img_bytes = base64.b64decode(b64_string)
    st.image(img_bytes, **kwargs)

st.set_page_config(
    page_title="Instalações Elitee | Elétrica & Hidráulica Profissional – DF",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

WHATSAPP_ICON = """<svg width="20" height="20" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" style="flex-shrink:0;vertical-align:middle;display:inline-block;">
  <path fill="white" d="M22.5 9.5C21 8 19 7 16.8 7C12.3 7 8.6 10.7 8.6 15.2C8.6 16.7 9 18.1 9.7 19.3L8.5 24L13.3 22.8C14.5 23.4 15.6 23.8 16.8 23.8C21.3 23.8 25 20.1 25 15.6C25 13.4 24 11.1 22.5 9.5ZM16.8 22.3C15.7 22.3 14.6 22 13.6 21.4L13.3 21.2L10.6 21.9L11.3 19.3L11.1 19C10.4 17.9 10 16.6 10 15.2C10 11.5 13.1 8.5 16.8 8.5C18.6 8.5 20.2 9.2 21.5 10.4C22.8 11.7 23.5 13.3 23.5 15.2C23.5 18.9 20.5 22.3 16.8 22.3ZM20.5 17C20.3 16.9 19.2 16.4 19 16.3C18.8 16.2 18.6 16.2 18.5 16.4C18.3 16.6 17.9 17.1 17.8 17.3C17.7 17.5 17.5 17.5 17.3 17.4C16.3 17 15.5 16.5 14.8 15.8C14.2 15.2 13.7 14.5 13.4 13.7C13.3 13.5 13.4 13.3 13.5 13.2C13.6 13.1 13.8 12.9 13.9 12.8C14 12.7 14.1 12.5 14.1 12.4C14.2 12.3 14.1 12.1 14.1 12C14 11.9 13.6 10.8 13.4 10.4C13.3 10 13.1 10.1 13 10.1H12.6C12.4 10.1 12.1 10.2 11.9 10.4C11.7 10.6 11.2 11.1 11.2 12.2C11.2 13.3 11.9 14.3 12 14.5C12.1 14.7 13.6 17.1 15.9 18.1C16.4 18.3 16.8 18.5 17.1 18.6C17.6 18.8 18.1 18.8 18.4 18.7C18.8 18.6 19.6 18.2 19.8 17.7C20 17.2 20 16.8 19.9 16.7L20.5 17Z"/>
</svg>"""

INSTAGRAM_ICON = """<svg width="20" height="20" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" style="flex-shrink:0;vertical-align:middle;display:inline-block;">
  <rect x="7" y="7" width="18" height="18" rx="5" stroke="white" stroke-width="2" fill="none"/>
  <circle cx="16" cy="16" r="5" stroke="white" stroke-width="2" fill="none"/>
  <circle cx="22" cy="10" r="1.4" fill="white"/>
</svg>"""

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Raleway:wght@300;400;600;700&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, .main, .block-container {
    background-color: #0a0a0a !important;
    color: #e8e8e8 !important;
    font-family: 'Raleway', sans-serif !important;
}

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
[data-testid="stToolbar"] { display: none; }

:root {
    --gold: #C9A84C;
    --gold-light: #E8D08A;
    --gold-dark: #8B6914;
    --black: #0a0a0a;
    --dark: #111111;
    --card: #161616;
    --border: rgba(201, 168, 76, 0.25);
    --text: #e8e8e8;
    --muted: #888888;
}

h1, h2, h3, h4 {
    font-family: 'Cormorant Garamond', serif !important;
    text-transform: uppercase;
    letter-spacing: 2px;
}

/* ===== BARRA TOPO ===== */
.topbar {
    background: #000;
    border-bottom: 1px solid var(--border);
    padding: 10px 40px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 13px;
    color: var(--gold);
    letter-spacing: 1px;
    flex-wrap: wrap;
    gap: 10px;
}

.topbar-info {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    align-items: center;
}

.topbar-info span {
    font-family: 'Raleway', sans-serif;
    font-weight: 600;
}

.topbar-buttons {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    align-items: center;
}

.topbar-btn-wa {
    color: #fff !important;
    font-family: 'Raleway', sans-serif;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
    padding: 7px 16px;
    border-radius: 4px;
    text-decoration: none !important;
    background: #25D366;
    display: inline-flex;
    align-items: center;
    gap: 7px;
    transition: all 0.2s;
    white-space: nowrap;
}

.topbar-btn-wa:hover { filter: brightness(1.1); color: #fff !important; }

.topbar-btn-ig {
    color: #fff !important;
    font-family: 'Raleway', sans-serif;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
    padding: 7px 16px;
    border-radius: 4px;
    text-decoration: none !important;
    background: linear-gradient(135deg, #833ab4, #fd1d1d, #fcb045);
    display: inline-flex;
    align-items: center;
    gap: 7px;
    transition: all 0.2s;
    white-space: nowrap;
}

.topbar-btn-ig:hover { filter: brightness(1.1); color: #fff !important; }

/* ===== HERO ===== */
.hero-wrapper {
    position: relative;
    width: 100%;
    min-height: 520px;
    overflow: hidden;
    display: flex;
    align-items: center;
}

.hero-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(
        105deg,
        rgba(0,0,0,0.97) 0%,
        rgba(0,0,0,0.85) 45%,
        rgba(0,0,0,0.4) 100%
    );
    z-index: 1;
}

.hero-content {
    position: relative;
    z-index: 2;
    padding: 60px 60px;
    max-width: 680px;
}

.hero-badge {
    display: inline-block;
    background: var(--gold);
    color: #000;
    font-family: 'Raleway', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 3px;
    padding: 5px 14px;
    text-transform: uppercase;
    margin-bottom: 20px;
}

.hero-title {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(40px, 5vw, 70px) !important;
    font-weight: 700 !important;
    line-height: 1.05 !important;
    color: #fff !important;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 16px !important;
}

.hero-title span { color: var(--gold); }

.hero-subtitle {
    font-family: 'Raleway', sans-serif;
    font-size: 17px;
    color: #bbb;
    line-height: 1.7;
    margin-bottom: 32px;
    font-weight: 300;
    max-width: 520px;
}

.hero-cta {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: linear-gradient(135deg, var(--gold) 0%, var(--gold-light) 100%);
    color: #000 !important;
    font-family: 'Raleway', sans-serif;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 16px 36px;
    border-radius: 3px;
    text-decoration: none !important;
    transition: all 0.25s;
    box-shadow: 0 4px 25px rgba(201,168,76,0.35);
}

.hero-cta:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 35px rgba(201,168,76,0.5);
    color: #000 !important;
}

.hero-stats {
    display: flex;
    gap: 40px;
    margin-top: 40px;
    padding-top: 30px;
    border-top: 1px solid rgba(255,255,255,0.1);
}

.stat-item { text-align: left; }

.stat-num {
    font-family: 'Cormorant Garamond', serif;
    font-size: 36px;
    font-weight: 700;
    color: var(--gold);
    line-height: 1;
}

.stat-label {
    font-family: 'Raleway', sans-serif;
    font-size: 11px;
    color: #777;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 4px;
    font-weight: 400;
}

/* ===== SECTIONS ===== */
.section {
    padding: 80px 60px;
    background: var(--black);
}

.section.alt { background: #0e0e0e; }

.section-tag {
    font-family: 'Raleway', sans-serif;
    font-size: 11px;
    letter-spacing: 4px;
    color: var(--gold);
    text-transform: uppercase;
    margin-bottom: 10px;
    display: block;
    font-weight: 600;
}

.section-title {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(32px, 3.5vw, 48px) !important;
    font-weight: 700 !important;
    color: #fff !important;
    text-transform: uppercase;
    letter-spacing: 2px;
    line-height: 1.1 !important;
    margin-bottom: 16px !important;
}

.section-title span { color: var(--gold); }

.section-desc {
    font-family: 'Raleway', sans-serif;
    font-size: 15px;
    color: var(--muted);
    line-height: 1.8;
    max-width: 600px;
    font-weight: 300;
    margin-bottom: 50px;
}

/* ===== DIFERENCIAIS ===== */
.diff-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2px;
}

.diff-card {
    background: var(--card);
    padding: 40px 32px;
    border-top: 3px solid var(--gold);
    transition: background 0.25s;
}

.diff-card:hover { background: #1c1c1c; }

.diff-icon {
    font-size: 32px;
    margin-bottom: 16px;
    display: block;
}

.diff-num {
    font-family: 'Cormorant Garamond', serif;
    font-size: 48px;
    font-weight: 700;
    color: var(--gold);
    line-height: 1;
    margin-bottom: 6px;
}

.diff-title {
    font-family: 'Raleway', sans-serif;
    font-size: 14px;
    font-weight: 700;
    color: #fff;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

.diff-text {
    font-family: 'Raleway', sans-serif;
    font-size: 14px;
    color: var(--muted);
    line-height: 1.7;
    font-weight: 300;
}

/* ===== SERVIÇOS ===== */
.service-panel {
    background: var(--card);
    padding: 0;
    overflow: hidden;
}

.service-img-wrapper {
    width: 100%;
    overflow: hidden;
    height: 260px;
    position: relative;
}

.service-img-wrapper img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.4s;
}

.service-panel:hover .service-img-wrapper img { transform: scale(1.04); }

.service-body { padding: 36px; }

.service-tag {
    display: inline-block;
    background: var(--gold);
    color: #000;
    font-family: 'Raleway', sans-serif;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 3px;
    padding: 4px 12px;
    text-transform: uppercase;
    margin-bottom: 14px;
}

.service-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 28px;
    font-weight: 700;
    color: #fff;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 20px;
    line-height: 1.2;
}

.service-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.service-list li {
    font-family: 'Raleway', sans-serif;
    font-size: 14px;
    color: #aaa;
    padding: 9px 0;
    border-bottom: 1px solid rgba(255,255,255,0.05);
    display: flex;
    align-items: center;
    gap: 10px;
    font-weight: 300;
}

.service-list li::before {
    content: '';
    width: 6px;
    height: 6px;
    background: var(--gold);
    border-radius: 50%;
    flex-shrink: 0;
}

/* ===== DICA ===== */
.dica-text-side {
    background: var(--gold);
    padding: 60px 50px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 100%;
}

.dica-text-side h2 {
    font-family: 'Cormorant Garamond', serif;
    font-size: 34px;
    font-weight: 700;
    color: #000 !important;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 20px;
}

.dica-text-side p {
    font-family: 'Raleway', sans-serif;
    font-size: 16px;
    color: #1a1a1a;
    line-height: 1.8;
    font-weight: 400;
}

.dica-text-side strong { color: #000; font-weight: 700; }

.dica-img-side {
    overflow: hidden;
    min-height: 360px;
}

/* ===== NORMA BANNER ===== */
.norma-banner {
    background: linear-gradient(135deg, #111 0%, #1a1500 100%);
    border: 1px solid var(--border);
    padding: 36px 40px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 24px;
    margin: 3px 0;
}

.norma-text h3 {
    font-family: 'Cormorant Garamond', serif;
    font-size: 22px;
    font-weight: 700;
    color: var(--gold) !important;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 8px;
}

.norma-text p {
    font-family: 'Raleway', sans-serif;
    font-size: 14px;
    color: #888;
    font-weight: 300;
    line-height: 1.6;
    max-width: 500px;
}

.norma-badges {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}

.norma-badge {
    background: rgba(201,168,76,0.1);
    border: 1px solid var(--gold);
    color: var(--gold);
    font-family: 'Raleway', sans-serif;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    padding: 10px 18px;
    text-transform: uppercase;
    white-space: nowrap;
}

/* ===== RODAPÉ ===== */
.footer {
    background: #050505;
    border-top: 1px solid var(--border);
    padding: 28px 60px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 12px;
}

.footer-copy {
    font-family: 'Raleway', sans-serif;
    font-size: 12px;
    color: #444;
    letter-spacing: 1px;
}

.footer-right {
    font-family: 'Raleway', sans-serif;
    font-size: 12px;
    color: #333;
    letter-spacing: 1px;
}

/* ===== MOBILE ===== */
@media (max-width: 768px) {
    .topbar { padding: 10px 16px; flex-direction: column; align-items: flex-start; gap: 10px; }
    .topbar-buttons { width: 100%; }
    .topbar-btn-wa, .topbar-btn-ig { flex: 1; justify-content: center; font-size: 11px; padding: 8px 10px; }
    .hero-content { padding: 40px 20px; }
    .hero-stats { gap: 20px; flex-wrap: wrap; }
    .diff-grid { grid-template-columns: 1fr; gap: 3px; }
    .dica-text-side { padding: 40px 24px; }
    .dica-img-side { min-height: 200px; }
    .norma-banner { padding: 28px 20px; flex-direction: column; align-items: flex-start; }
    .norma-badges { width: 100%; }
    .section { padding: 50px 20px; }
    .footer { padding: 20px; flex-direction: column; text-align: center; }
}

/* ===== STREAMLIT OVERRIDES ===== */
.stButton > button {
    background: linear-gradient(135deg, var(--gold) 0%, var(--gold-light) 100%) !important;
    color: #000 !important;
    font-family: 'Raleway', sans-serif !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    border: none !important;
    padding: 18px 36px !important;
    border-radius: 3px !important;
    width: 100% !important;
    box-shadow: 0 4px 20px rgba(201,168,76,0.3) !important;
    transition: all 0.25s !important;
}

.stLinkButton > a {
    background: #25D366 !important;
    color: #fff !important;
    font-family: 'Raleway', sans-serif !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    border: none !important;
    padding: 18px 36px !important;
    border-radius: 3px !important;
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    box-shadow: 0 4px 20px rgba(37,211,102,0.3) !important;
}

[data-testid="stImage"] { display: block; }
[data-testid="stVerticalBlock"] { gap: 0 !important; }
.st-emotion-cache-z5fcl4 { padding: 0 !important; }
div[data-testid="column"] { padding: 0 !important; }
.element-container { margin-bottom: 0 !important; }
</style>
""", unsafe_allow_html=True)


# ==============================
# TOPBAR
# ==============================
st.markdown(f"""
<div class="topbar">
    <div class="topbar-info">
        <span>📍 Atendemos todo o DF e Entorno</span>
        <span>⚡ Elétrica &nbsp;|&nbsp; 💧 Hidráulica</span>
        <span>🏗️ NBR-5410 Certificado</span>
    </div>
    <div class="topbar-buttons">
        <a class="topbar-btn-wa" href="https://wa.me/5561992473134" target="_blank">
            {WHATSAPP_ICON} ORÇAMENTO GRÁTIS
        </a>
        <a class="topbar-btn-ig" href="https://www.instagram.com/instalacoes_elitee?igsh=MTRtbjF3NWh5cmk2aw==" target="_blank">
            {INSTAGRAM_ICON} INSTAGRAM
        </a>
    </div>
</div>
""", unsafe_allow_html=True)


# ==============================
# HERO SECTION
# ==============================
hero_col, _ = st.columns([1, 0.001])
with hero_col:
    img_bytes_destaque = base64.b64decode(IMG_DESTAQUE)
    b64_bg = base64.b64encode(img_bytes_destaque).decode()

    st.markdown(f"""
    <div class="hero-wrapper" style="background: url('data:image/jpeg;base64,{b64_bg}') center/cover no-repeat; min-height: 560px;">
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <div class="hero-badge">⚡ Especialistas no Distrito Federal</div>
            <h1 class="hero-title">
                INSTALAÇÕES<br>
                <span>ELITEE</span><br>
                ELÉTRICA &amp; HIDRÁULICA
            </h1>
            <p class="hero-subtitle">
                Referência técnica em serviços elétricos e hidráulicos para 
                residências e condomínios no DF e Entorno. 
                Qualidade comprovada com mais de 20 anos de experiência.
            </p>
            <a href="https://wa.me/5561992473134" class="hero-cta" target="_blank">
                📲 FALAR COM O TÉCNICO KLEBER
            </a>
            <div class="hero-stats">
                <div class="stat-item">
                    <div class="stat-num">20+</div>
                    <div class="stat-label">Anos de mercado</div>
                </div>
                <div class="stat-item">
                    <div class="stat-num">500+</div>
                    <div class="stat-label">Obras entregues</div>
                </div>
                <div class="stat-item">
                    <div class="stat-num">NBR</div>
                    <div class="stat-label">5410 Certificado</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ==============================
# NORMA BANNER
# ==============================
st.markdown("""
<div class="norma-banner">
    <div class="norma-text">
        <h3>Trabalhamos Dentro das Normas Técnicas</h3>
        <p>Todos os serviços são executados com rigor técnico e seguindo as regulamentações vigentes, 
        garantindo segurança, durabilidade e conformidade legal para o seu imóvel.</p>
    </div>
    <div class="norma-badges">
        <div class="norma-badge">NBR 5410</div>
        <div class="norma-badge">NR 10</div>
        <div class="norma-badge">ABNT</div>
        <div class="norma-badge">INMETRO</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ==============================
# DIFERENCIAIS
# ==============================
st.markdown("""
<div class="section">
    <span class="section-tag">Por que nos escolher</span>
    <h2 class="section-title">Nossos <span>Diferenciais</span></h2>
    <p class="section-desc">
        Quando o assunto é a segurança do seu imóvel, não dá para arriscar. 
        A Elitee entrega mais do que um serviço — entrega tranquilidade.
    </p>
    <div class="diff-grid">
        <div class="diff-card">
            <span class="diff-icon">🏆</span>
            <div class="diff-num">20+</div>
            <div class="diff-title">Anos de Experiência</div>
            <p class="diff-text">Experiência acumulada em centenas de obras residenciais e prediais em todo o Distrito Federal.</p>
        </div>
        <div class="diff-card">
            <span class="diff-icon">🛡️</span>
            <div class="diff-num">100%</div>
            <div class="diff-title">Segurança &amp; Normas</div>
            <p class="diff-text">Rigorosamente dentro das normas NBR-5410, NR-10 e padrões técnicos da CEB e CAESB.</p>
        </div>
        <div class="diff-card">
            <span class="diff-icon">✅</span>
            <div class="diff-num">Garantia</div>
            <div class="diff-title">Pós-serviço Incluso</div>
            <p class="diff-text">Acompanhamento técnico após a entrega do serviço e compromisso com a durabilidade da obra.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ==============================
# SERVIÇOS
# ==============================
st.markdown("""
<div class="section alt">
    <span class="section-tag">O que fazemos</span>
    <h2 class="section-title">Nossas <span>Especialidades</span></h2>
    <p class="section-desc">
        Soluções completas de elétrica e hidráulica para residências, 
        condomínios e obras comerciais.
    </p>
</div>
""", unsafe_allow_html=True)

col_e, col_h = st.columns(2)

with col_e:
    st.markdown("""
    <div class="service-panel">
        <div class="service-img-wrapper">
    """, unsafe_allow_html=True)
    show_img(IMG_ELETRICA, use_container_width=True)
    st.markdown("""
        </div>
        <div class="service-body">
            <span class="service-tag">Elétrica</span>
            <div class="service-title">Elétrica Predial<br>e Residencial</div>
            <ul class="service-list">
                <li>Instalação de Quadros de Distribuição</li>
                <li>Manutenção de Sistemas de Bombas</li>
                <li>Infraestrutura Completa para Condomínios</li>
                <li>Iluminação e Automação Residencial</li>
                <li>Laudo Técnico e ART Elétrica</li>
                <li>Adequação ao Padrão CEB</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_h:
    st.markdown("""
    <div class="service-panel">
        <div class="service-img-wrapper">
    """, unsafe_allow_html=True)
    show_img(IMG_HIDRAULICA, use_container_width=True)
    st.markdown("""
        </div>
        <div class="service-body">
            <span class="service-tag">Hidráulica</span>
            <div class="service-title">Hidráulica e<br>Sistemas de Água</div>
            <ul class="service-list">
                <li>Reparo de Vazamentos Estruturais</li>
                <li>Manutenção Preventiva de Bombas</li>
                <li>Limpeza e Vedação de Reservatórios</li>
                <li>Redes de Incêndio e Sistemas de Recalque</li>
                <li>Alinhamento Técnico de Tubulações</li>
                <li>Adequação ao Padrão CAESB</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ==============================
# DICA DA ELITEE
# ==============================
col_dica_txt, col_dica_img = st.columns(2)

with col_dica_txt:
    st.markdown("""
    <div class="dica-text-side">
        <h2>💡 Dica da Elitee</h2>
        <p>
            <strong>Prevenção é a melhor economia.</strong> Uma revisão periódica no quadro elétrico pode 
            evitar incêndios e reduzir sua conta de energia em até 20%.<br><br>
            Não arrisque seu patrimônio contratando serviços improvisados. 
            No DF, existe padrão técnico exigido pela CEB e pela CAESB — 
            e a Elitee conhece cada detalhe dessas normas.<br><br>
            <strong>Contrate quem tem histórico, técnica e responsabilidade.</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_dica_img:
    st.markdown('<div class="dica-img-side">', unsafe_allow_html=True)
    show_img(IMG_DICAS, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ==============================
# CONTATO
# ==============================
col_ctxt, col_cimg = st.columns(2)

with col_ctxt:
    st.markdown("""
    <div style="background:#000; padding: 80px 50px; border-top: 3px solid #C9A84C;">
        <h2 style="font-family:'Cormorant Garamond',serif; font-size:clamp(28px,3.5vw,48px); font-weight:700; color:#fff !important; text-transform:uppercase; letter-spacing:2px; line-height:1.1; margin-bottom:16px;">
            SOLICITE SEU<br><span style="color:#C9A84C;">ORÇAMENTO GRÁTIS</span>
        </h2>
        <p style="font-family:'Raleway',sans-serif; font-size:15px; color:#888; line-height:1.8; font-weight:300; margin-bottom:28px;">
            Atendimento rápido e personalizado. Resposta em menos de 1 hora 
            via WhatsApp nos dias úteis.
        </p>
        <div style="display:flex; flex-direction:column; gap:14px; margin-bottom:32px;">
            <div style="display:flex; align-items:center; gap:14px; font-family:'Raleway',sans-serif; font-size:14px; color:#bbb;">
                <div style="width:38px; height:38px; background:rgba(201,168,76,0.1); border:1px solid rgba(201,168,76,0.25); display:flex; align-items:center; justify-content:center; font-size:16px; flex-shrink:0;">📞</div>
                <span>(61) 99247-3134 — Kleber</span>
            </div>
            <div style="display:flex; align-items:center; gap:14px; font-family:'Raleway',sans-serif; font-size:14px; color:#bbb;">
                <div style="width:38px; height:38px; background:rgba(201,168,76,0.1); border:1px solid rgba(201,168,76,0.25); display:flex; align-items:center; justify-content:center; font-size:16px; flex-shrink:0;">📍</div>
                <span>DF e Cidades do Entorno</span>
            </div>
            <div style="display:flex; align-items:center; gap:14px; font-family:'Raleway',sans-serif; font-size:14px; color:#bbb;">
                <div style="width:38px; height:38px; background:rgba(201,168,76,0.1); border:1px solid rgba(201,168,76,0.25); display:flex; align-items:center; justify-content:center; font-size:16px; flex-shrink:0;">🕐</div>
                <span>Seg a Sáb — 07h às 19h</span>
            </div>
            <div style="display:flex; align-items:center; gap:14px; font-family:'Raleway',sans-serif; font-size:14px; color:#bbb;">
                <div style="width:38px; height:38px; background:rgba(201,168,76,0.1); border:1px solid rgba(201,168,76,0.25); display:flex; align-items:center; justify-content:center; font-size:16px; flex-shrink:0;">📸</div>
                <a href="https://www.instagram.com/instalacoes_elitee?igsh=MTRtbjF3NWh5cmk2aw==" target="_blank" style="color:#C9A84C; text-decoration:none; font-family:'Raleway',sans-serif; font-weight:600;">@instalacoes_elitee</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("📲 FALAR NO WHATSAPP AGORA", "https://wa.me/5561992473134")

with col_cimg:
    st.markdown('<div style="background:#0e0e0e; height:100%; display:flex; align-items:center; justify-content:center; padding:40px;">', unsafe_allow_html=True)
    show_img(IMG_INFORMACOES, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ==============================
# RODAPÉ
# ==============================
st.markdown("""
<div class="footer">
    <div class="footer-copy">© 2026 Instalações Elitee · Todos os direitos reservados · Responsável Técnico: Kleber</div>
    <div class="footer-right">⚡ Elétrica &nbsp;|&nbsp; 💧 Hidráulica &nbsp;|&nbsp; 📍 Distrito Federal</div>
</div>
""", unsafe_allow_html=True)
