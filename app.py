import streamlit as st

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
