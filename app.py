import streamlit as st

# Configuração da página
st.set_page_config(page_title="Instalações Elitee", page_icon="⚡", layout="wide")

# CSS para o visual Preto e Dourado
st.markdown("""
    <style>
    .main { background-color: #000000; color: #FFFFFF; }
    h1, h2, h3 { color: #D4AF37 !important; }
    .stButton>button { background-color: #D4AF37; color: black; font-weight: bold; width: 100%; border-radius: 10px; }
    .card { border: 1px solid #D4AF37; padding: 20px; border-radius: 15px; margin-bottom: 20px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- TOPO / LOGO ---
col_logo1, col_logo2, col_logo3 = st.columns([1, 2, 1])
with col_logo2:
    try:
        st.image("logo.png", width=300)
    except:
        st.markdown("<h1 style='text-align: center;'>⚡ INSTALAÇÕES ELITEE</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; font-size: 22px;'>Elétrica e Hidráulica com Eficiência e Qualidade</p>", unsafe_allow_html=True)
st.divider()

# --- SOBRE ---
c1, c2 = st.columns(2)
with c1:
    st.header("🏆 Mais de 20 anos de experiência")
    st.write("Referência em serviços prediais e residenciais no DF e Entorno. Especialista em centros de medição e organização técnica.")
    st.markdown("✅ **Qualidade** | ✅ **Segurança** | ✅ **Garantia**")
with c2:
    st.info("Eletricista Responsável: Kleber")

# --- GALERIA DE SERVIÇOS ---
st.header("🎯 Nossas Especialidades")
col_img1, col_img2 = st.columns(2)

with col_img1:
    try:
        st.image("eletrica.jpg", caption="Grandes Projetos e Infraestrutura Elétrica")
    except:
        st.warning("Imagem elétrica.jpg não encontrada")

with col_img2:
    try:
        st.image("hidraulica.jpg", caption="Sistemas de Bombas e Redes Hidráulicas")
    except:
        st.warning("Imagem hidraulica.jpg não encontrada")

# --- DICAS ---
st.divider()
col_dica1, col_dica2 = st.columns([1, 2])
with col_dica1:
    st.header("💡 Dicas da Elitee")
    st.write("Contrate sempre profissionais capacitados para evitar riscos e desperdícios.")
with col_dica2:
    try:
        st.image("dicas.jpg", use_column_width=True)
    except:
        st.info("Imagem dicas.jpg não encontrada")

# --- CONTATO ---
st.divider()
st.header("📞 Fale Conosco")
st.write("📱 (61) 99247-3134 | 📧 instalacoes.eliteedf@gmail.com")
st.markdown(f"[![Botão WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/5561992473134)")

st.markdown("<br><center>© 2024 Instalações Elitee - DF e Entorno</center>", unsafe_allow_html=True)
