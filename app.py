import streamlit as st
import os

# Caminho base onde estão as imagens (mesma pasta do app.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def img(nome, **kwargs):
    caminho = os.path.join(BASE_DIR, nome)
    if os.path.exists(caminho):
        st.image(caminho, **kwargs)
        return True
    return False

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
    if not img("logo.jpg", width=250):
        st.subheader("⚡ INSTALAÇÕES ELITEE")

st.markdown("<h1 style='text-align: center; font-size: 50px;'>SOLUÇÕES ELITE PARA SEU IMÓVEL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 22px; color: #aaa;'>Referência em Engenharia Elétrica e Hidráulica no Distrito Federal e Entorno</p>", unsafe_allow_html=True)

# Imagem de Destaque (Banner Principal)
if not img("destaque.jpg", use_container_width=True):
    st.divider()

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
    if not img("eletrica.jpg", caption="Quadros de Energia e Centros de Medição", use_container_width=True):
        st.info("Imagem de Elétrica")
    st.write("""
    - Instalação de Quadros de Distribuição
    - Manutenção de Sistemas de Bombas
    - Infraestrutura Completa para Condomínios
    - Iluminação e Automação
    """)

with col_hidra:
    st.subheader("💧 Hidráulica e Sistemas")
    if not img("hidraulica.jpg", caption="Redes de Incêndio e Sistemas de Recalque", use_container_width=True):
        st.info("Imagem de Hidráulica")
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
    img("dicas.jpg", use_container_width=True)

# --- CONTATO E RODAPÉ ---
st.divider()
st.header("📲 Solicite seu Orçamento Gratuito")
col_zap, col_contato = st.columns([1, 1])

with col_zap:
    st.markdown("### Atendimento Imediato")
    st.link_button("FALAR COM O TÉCNICO KLEBER", "https://wa.me/5561992473134")
    st.write("📍 Atendemos todo o DF e Cidades do Entorno.")

with col_contato:
    if not img("informacoescontato.jpg", width=400):
        st.write("📱 (61) 99247-3134")
        st.write("📧 instalacoes.eliteedf@gmail.com")

st.markdown("<br><hr><center><p style='color: #666;'>© 2026 Instalações Elitee. Todos os direitos reservados. Eletricista Responsável: Kleber.</p></center>", unsafe_allow_html=True)
