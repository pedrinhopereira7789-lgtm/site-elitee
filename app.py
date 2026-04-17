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

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@400;600;700&family=Lato:wght@300;400;700&display=swap');

/* ===== RESET & BASE ===== */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, .main, .block-container {
    background-color: #0a0a0a !important;
    color: #e8e8e8 !important;
    font-family: 'Lato', sans-serif !important;
}

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* Esconde elementos desnecessários do Streamlit */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
[data-testid="stToolbar"] { display: none; }

/* ===== VARIÁVEIS DE COR ===== */
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

/* ===== TIPOGRAFIA ===== */
h1, h2, h3, h4 {
    font-family: 'Oswald', sans-serif !important;
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
}

.topbar span { margin-right: 20px; }
.topbar a {
    color: var(--gold);
    text-decoration: none;
    font-weight: 700;
    padding: 6px 18px;
    border: 1px solid var(--gold);
    border-radius: 3px;
    transition: all 0.2s;
}
.topbar a:hover { background: var(--gold); color: #000; }

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
    font-family: 'Oswald', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 3px;
    padding: 5px 14px;
    text-transform: uppercase;
    margin-bottom: 20px;
}

.hero-title {
    font-family: 'Oswald', sans-serif !important;
    font-size: clamp(36px, 5vw, 64px) !important;
    font-weight: 700 !important;
    line-height: 1.05 !important;
    color: #fff !important;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 16px !important;
}

.hero-title span { color: var(--gold); }

.hero-subtitle {
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
    font-family: 'Oswald', sans-serif;
    font-size: 16px;
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
    font-family: 'Oswald', sans-serif;
    font-size: 32px;
    font-weight: 700;
    color: var(--gold);
    line-height: 1;
}
.stat-label {
    font-size: 11px;
    color: #777;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 4px;
}

/* ===== SECTION WRAPPER ===== */
.section {
    padding: 80px 60px;
    background: var(--black);
}

.section.alt { background: #0e0e0e; }

.section-tag {
    font-family: 'Oswald', sans-serif;
    font-size: 11px;
    letter-spacing: 4px;
    color: var(--gold);
    text-transform: uppercase;
    margin-bottom: 10px;
    display: block;
}

.section-title {
    font-family: 'Oswald', sans-serif !important;
    font-size: clamp(28px, 3.5vw, 42px) !important;
    font-weight: 700 !important;
    color: #fff !important;
    text-transform: uppercase;
    letter-spacing: 1px;
    line-height: 1.1 !important;
    margin-bottom: 16px !important;
}

.section-title span { color: var(--gold); }

.section-desc {
    font-size: 15px;
    color: var(--muted);
    line-height: 1.8;
    max-width: 600px;
    font-weight: 300;
    margin-bottom: 50px;
}

/* ===== CARDS DIFERENCIAIS ===== */
.diff-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2px;
    margin-top: 0;
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
    font-family: 'Oswald', sans-serif;
    font-size: 42px;
    font-weight: 700;
    color: var(--gold);
    line-height: 1;
    margin-bottom: 6px;
}

.diff-title {
    font-family: 'Oswald', sans-serif;
    font-size: 16px;
    font-weight: 600;
    color: #fff;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 10px;
}

.diff-text {
    font-size: 14px;
    color: var(--muted);
    line-height: 1.7;
    font-weight: 300;
}

/* ===== SERVIÇOS ===== */
.service-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3px;
}

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

.service-panel:hover .service-img-wrapper img {
    transform: scale(1.04);
}

.service-body { padding: 36px; }

.service-tag {
    display: inline-block;
    background: var(--gold);
    color: #000;
    font-family: 'Oswald', sans-serif;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 3px;
    padding: 4px 12px;
    text-transform: uppercase;
    margin-bottom: 14px;
}

.service-title {
    font-family: 'Oswald', sans-serif;
    font-size: 24px;
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
.dica-wrapper {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3px;
    align-items: stretch;
}

.dica-text-side {
    background: var(--gold);
    padding: 60px 50px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.dica-text-side h2 {
    font-family: 'Oswald', sans-serif;
    font-size: 32px;
    font-weight: 700;
    color: #000 !important;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 20px;
}

.dica-text-side p {
    font-size: 16px;
    color: #1a1a1a;
    line-height: 1.8;
    font-weight: 400;
}

.dica-text-side strong { color: #000; }

.dica-img-side {
    overflow: hidden;
    min-height: 360px;
}

/* ===== NORMA BANNER ===== */
.norma-banner {
    background: linear-gradient(135deg, #111 0%, #1a1500 100%);
    border: 1px solid var(--border);
    padding: 40px 60px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 30px;
    margin: 3px 0;
}

.norma-text h3 {
    font-family: 'Oswald', sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: var(--gold) !important;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 8px;
}

.norma-text p {
    font-size: 14px;
    color: #888;
    font-weight: 300;
    line-height: 1.6;
}

.norma-badges {
    display: flex;
    gap: 12px;
    flex-shrink: 0;
    flex-wrap: wrap;
}

.norma-badge {
    background: rgba(201,168,76,0.1);
    border: 1px solid var(--gold);
    color: var(--gold);
    font-family: 'Oswald', sans-serif;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    padding: 10px 20px;
    text-transform: uppercase;
}

/* ===== CONTATO ===== */
.contato-section {
    background: #000;
    padding: 80px 60px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: center;
    border-top: 3px solid var(--gold);
}

.contato-left h2 {
    font-family: 'Oswald', sans-serif;
    font-size: clamp(28px, 3.5vw, 44px);
    font-weight: 700;
    color: #fff !important;
    text-transform: uppercase;
    letter-spacing: 1px;
    line-height: 1.1;
    margin-bottom: 16px;
}

.contato-left h2 span { color: var(--gold); }

.contato-left p {
    font-size: 15px;
    color: #888;
    line-height: 1.8;
    font-weight: 300;
    margin-bottom: 32px;
}

.contato-info {
    display: flex;
    flex-direction: column;
    gap: 14px;
    margin-bottom: 32px;
}

.contato-item {
    display: flex;
    align-items: center;
    gap: 14px;
    font-size: 14px;
    color: #bbb;
}

.contato-item-icon {
    width: 38px;
    height: 38px;
    background: rgba(201,168,76,0.1);
    border: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    flex-shrink: 0;
}

.btn-whatsapp {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: #25D366;
    color: #fff !important;
    font-family: 'Oswald', sans-serif;
    font-size: 16px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 18px 36px;
    border-radius: 3px;
    text-decoration: none !important;
    transition: all 0.25s;
    box-shadow: 0 4px 20px rgba(37,211,102,0.3);
}

.btn-whatsapp:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(37,211,102,0.45);
    color: #fff !important;
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
    font-size: 12px;
    color: #444;
    letter-spacing: 1px;
}

.footer-right {
    font-size: 12px;
    color: #333;
    letter-spacing: 1px;
}

/* ===== STREAMLIT OVERRIDES ===== */
.stButton > button {
    background: linear-gradient(135deg, var(--gold) 0%, var(--gold-light) 100%) !important;
    color: #000 !important;
    font-family: 'Oswald', sans-serif !important;
    font-weight: 700 !important;
    font-size: 16px !important;
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
    font-family: 'Oswald', sans-serif !important;
    font-weight: 700 !important;
    font-size: 16px !important;
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

/* Remove espaços entre seções */
.element-container { margin-bottom: 0 !important; }
</style>
""", unsafe_allow_html=True)


# ==============================
# TOPBAR
# ==============================
st.markdown("""
<div class="topbar">
    <div>
        <span>📍 Atendemos todo o DF e Entorno</span>
        <span>⚡ Elétrica &nbsp;|&nbsp; 💧 Hidráulica</span>
        <span>🏗️ NBR-5410 Certificado</span>
    </div>
    <a href="https://wa.me/5561992473134" target="_blank">📲 ORÇAMENTO GRÁTIS</a>
</div>
""", unsafe_allow_html=True)


# ==============================
# HERO SECTION
# ==============================
hero_col, _ = st.columns([1, 0.001])
with hero_col:
    # Renderiza a imagem de fundo como base64 inline no CSS
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
                ELÉTRICA & HIDRÁULICA
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
            <div class="diff-title">Segurança & Normas</div>
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
    <div class="contato-section" style="display:block; padding: 80px 50px;">
        <h2 style="font-family:'Oswald',sans-serif; font-size:clamp(28px,3.5vw,42px); font-weight:700; color:#fff !important; text-transform:uppercase; letter-spacing:1px; line-height:1.1; margin-bottom:16px;">
            SOLICITE SEU<br><span style="color:#C9A84C;">ORÇAMENTO GRÁTIS</span>
        </h2>
        <p style="font-size:15px; color:#888; line-height:1.8; font-weight:300; margin-bottom:28px;">
            Atendimento rápido e personalizado. Resposta em menos de 1 hora 
            via WhatsApp nos dias úteis.
        </p>
        <div style="display:flex; flex-direction:column; gap:14px; margin-bottom:32px;">
            <div style="display:flex; align-items:center; gap:14px; font-size:14px; color:#bbb;">
                <div style="width:38px; height:38px; background:rgba(201,168,76,0.1); border:1px solid rgba(201,168,76,0.25); display:flex; align-items:center; justify-content:center; font-size:16px; flex-shrink:0;">📞</div>
                <span>(61) 99247-3134 — Kleber</span>
            </div>
            <div style="display:flex; align-items:center; gap:14px; font-size:14px; color:#bbb;">
                <div style="width:38px; height:38px; background:rgba(201,168,76,0.1); border:1px solid rgba(201,168,76,0.25); display:flex; align-items:center; justify-content:center; font-size:16px; flex-shrink:0;">📍</div>
                <span>DF e Cidades do Entorno</span>
            </div>
            <div style="display:flex; align-items:center; gap:14px; font-size:14px; color:#bbb;">
                <div style="width:38px; height:38px; background:rgba(201,168,76,0.1); border:1px solid rgba(201,168,76,0.25); display:flex; align-items:center; justify-content:center; font-size:16px; flex-shrink:0;">🕐</div>
                <span>Seg a Sáb — 07h às 19h</span>
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
# LOGO + RODAPÉ
# ==============================
st.markdown("""
<div class="footer">
    <div class="footer-copy">© 2026 Instalações Elitee · Todos os direitos reservados · Responsável Técnico: Kleber</div>
    <div class="footer-right">⚡ Elétrica &nbsp;|&nbsp; 💧 Hidráulica &nbsp;|&nbsp; 📍 Distrito Federal</div>
</div>
""", unsafe_allow_html=True)
