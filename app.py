import streamlit as stimport streamlit as st

# Configuração da página
st.set_page_config(page_title="Instalações Elitee", page_icon="⚡", layout="wide")

# CSS Personalizado para o tema Preto e Dourado
st.markdown("""
    <style>
    .main {
        background-color: #000000;
        color: #FFFFFF;
    }
    h1, h2, h3 {
        color: #D4AF37 !important; /* Dourado */
    }
    .stButton>button {
        background-color: #D4AF37;
        color: black;
        border-radius: 10px;
        font-weight: bold;
        width: 100%;
    }
    .card {
        border: 1px solid #D4AF37;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 20px;
    }
    .footer {
        text-align: center;
        color: #D4AF37;
        padding: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO / HERO ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("sua_logo_redonda.png", width=250) # Substitua pelo arquivo da logo
    st.markdown("<h1 style='text-align: center;'>INSTALAÇÕES ELITEE</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px;'>Elétrica e Hidráulica com Eficiência e Qualidade</p>", unsafe_allow_html=True)

st.divider()

# --- SEÇÃO SOBRE ---
col_desc1, col_desc2 = st.columns(2)
with col_desc1:
    st.header("🏆 Há mais de 20 anos no mercado")
    st.write("""
        A Instalações Elitee é referência em serviços prediais e residenciais no DF e Entorno. 
        Nosso foco é a organização técnica e a segurança total do seu patrimônio.
    """)
    st.markdown("✅ **Qualidade** | ✅ **Segurança** | ✅ **Garantia**")
    
with col_desc2:
    # Espaço para uma das fotos de obras (ex: quadros elétricos)
    st.info("Eletricista Responsável: Kleber")

# --- SEÇÃO SERVIÇOS ---
st.header("🎯 Nossas Especialidades")
col_srv1, col_srv2, col_srv3 = st.columns(3)

with col_srv1:
    st.markdown("""<div class='card'>
        <h3>⚡ Elétrica</h3>
        <p>Centros de medição, instalação de quadros, infraestrutura completa e manutenção preventiva.</p>
    </div>""", unsafe_allow_html=True)

with col_srv2:
    st.markdown("""<div class='card'>
        <h3>💧 Hidráulica</h3>
        <p>Sistemas de bombas e redes, reparo de vazamentos e alinhamento técnico de tubulações.</p>
    </div>""", unsafe_allow_html=True)

with col_srv3:
    st.markdown("""<div class='card'>
        <h3>🏢 Predial & Residencial</h3>
        <p>Atendimento especializado para condomínios e residências de alto padrão no DF.</p>
    </div>""", unsafe_allow_html=True)

# --- DICAS DO DIA A DIA ---
st.header("💡 Dicas da Elitee")
t1, t2, t3 = st.tabs(["Prevenção", "Segurança", "Economia"])
with t1:
    st.write("Evite vazamentos através da manutenção preventiva regular.")
with t2:
    st.write("Não sobrecarregue as tomadas com vários equipamentos (benjamins/tês).")
with t3:
    st.write("Contrate sempre um profissional capacitado para evitar gastos desnecessários com retrabalho.")

# --- CONTATO ---
st.divider()
st.header("📞 Entre em Contato")
c1, c2, c3 = st.columns(3)
with c1:
    st.button("💬 Chamar no WhatsApp")
with c2:
    st.write("📧 instalacoes.eliteedf@gmail.com")
with c3:
    st.write("📱 (61) 99247-3134")

st.markdown("<div class='footer'>© 2024 Instalações Elitee - DF e Entorno</div>", unsafe_allow_html=True)
import base64
from img_data import IMG_LOGO, IMG_DESTAQUE, IMG_ELETRICA, IMG_HIDRAULICA, IMG_DICAS, IMG_INFORMACOES

def show_img(b64_string, **kwargs):
    """Exibe imagem a partir de string base64"""
    img_bytes = base64.b64decode(b64_string)
    st.image(img_bytes, **kwargs)

# Configuração Master da Página
st.set_page_config(
    page_title="Instalações Elitee | Elétrica & Hidráulica Profissional",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilização CSS Avançada (Padrão Black & Gold)
st.markdown("""
    <style>
    /* Fundo e Texto Geral */
    .main { background-color: #0b0b0b; color: #f0f0f0; }
    
    /* Títulos em Dourado */
    h1, h2, h3 { 
        color: #D4AF37 !important; 
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 700 !important;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* Estilo dos Cards de Serviço */
    .service-card {
        background-color: #1a1a1a;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #D4AF37;
        text-align: center;
        transition: 0.3s;
    }
    
    /* Botão WhatsApp Flutuante/Destaque */
    .stButton>button {
        background: linear-gradient(45deg, #D4AF37, #F3E5AB);
        color: #000 !important;
        font-weight: bold !important;
        border: none !important;
        padding: 15px 30px !important;
        border-radius: 50px !important;
        width: 100%;
        font-size: 20px !important;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
    }
    
    /* Divisores Dourados */
    hr { border-top: 2px solid #D4AF37 !important; opacity: 0.5; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO / HERO ---
col_logo, col_vazio = st.columns([1, 2])
with col_logo:
    show_img(IMG_LOGO, width=250)

st.markdown("<h1 style='text-align: center; font-size: 50px;'>SOLUÇÕES ELITE PARA SEU IMÓVEL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 22px; color: #aaa;'>Referência em Engenharia Elétrica e Hidráulica no Distrito Federal e Entorno</p>", unsafe_allow_html=True)

# Imagem de Destaque (Banner Principal)
show_img(IMG_DESTAQUE, use_container_width=True)

# --- DIFERENCIAIS ---
st.write("")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("<div class='service-card'><h3>20+ Anos</h3><p>Experiência comprovada em grandes obras prediais e residenciais.</p></div>", unsafe_allow_html=True)
with c2:
    st.markdown("<div class='service-card'><h3>Segurança</h3><p>Seguimos rigorosamente as normas NBR-5410 e padrões técnicos.</p></div>", unsafe_allow_html=True)
with c3:
    st.markdown("<div class='service-card'><h3>Garantia</h3><p>Suporte técnico pós-serviço e compromisso com a durabilidade.</p></div>", unsafe_allow_html=True)

st.divider()

# --- GALERIA DE SERVIÇOS ---
st.header("🎯 Nossas Especialidades")
col_elet, col_hidra = st.columns(2)

with col_elet:
    st.subheader("⚡ Elétrica Predial e Residencial")
    show_img(IMG_ELETRICA, caption="Quadros de Energia e Centros de Medição", use_container_width=True)
    st.write("""
    - Instalação de Quadros de Distribuição
    - Manutenção de Sistemas de Bombas
    - Infraestrutura Completa para Condomínios
    - Iluminação e Automação
    """)

with col_hidra:
    st.subheader("💧 Hidráulica e Sistemas")
    show_img(IMG_HIDRAULICA, caption="Redes de Incêndio e Sistemas de Recalque", use_container_width=True)
    st.write("""
    - Reparo de Vazamentos Estruturais
    - Manutenção Preventiva de Bombas
    - Limpeza e Vedação de Reservatórios
    - Alinhamento Técnico de Tubulações
    """)

# --- SEÇÃO DE DICAS ---
st.divider()
col_d, col_img_d = st.columns([1, 1])
with col_d:
    st.header("💡 Dicas da Elitee")
    st.markdown("""
    **Prevenção é economia!**
    Muitas vezes, uma simples revisão no quadro elétrico evita incêndios e reduz sua conta de luz em até 20%.
    
    *Não arrisque seu patrimônio com curiosos. Contrate quem entende do padrão DF.*
    """)
with col_img_d:
    show_img(IMG_DICAS, use_container_width=True)

# --- CONTATO E RODAPÉ ---
st.divider()
st.header("📲 Solicite seu Orçamento Gratuito")
col_zap, col_contato = st.columns([1, 1])

with col_zap:
    st.markdown("### Atendimento Imediato")
    st.link_button("FALAR COM O TÉCNICO KLEBER", "https://wa.me/5561992473134")
    st.write("📍 Atendemos todo o DF e Cidades do Entorno.")

with col_contato:
    show_img(IMG_INFORMACOES, width=400)

st.markdown("<br><hr><center><p style='color: #666;'>© 2026 Instalações Elitee. Todos os direitos reservados. Eletricista Responsável: Kleber.</p></center>", unsafe_allow_html=True)
