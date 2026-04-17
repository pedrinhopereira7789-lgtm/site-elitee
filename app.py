import streamlit as st
# ── Configuração da página ──────────────────────────────────────────────────
st.set_page_config(
    # TAG DE VERIFICAÇÃO GOOGLE
st.markdown("""
    <meta name="google-site-verification" content="gCNlCNMPOTcoPzQvAPbx-5Thz1u6oBsQqNbOMGhVLsU" />
""", unsafe_allow_html=True)
    page_title="Instalações Elitee | Elétrica & Hidráulica",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def img_tag(b64, alt="", style="width:100%;border-radius:4px;"):
    return f'<img src="data:image/jpeg;base64,{b64}" alt="{alt}" style="{style}"/>'

# ── CSS Global ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Barlow:wght@300;400;600;700&display=swap');

* { box-sizing: border-box; }
.main { background-color: #0a0a0a !important; color: #f5f5f2; }
section[data-testid="stSidebar"] { display: none; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

h1, h2, h3 {
    font-family: 'Bebas Neue', 'Arial Black', sans-serif !important;
    color: #C9A84C !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
}

.stLinkButton > a {
    background: linear-gradient(135deg, #25D366, #128C7E) !important;
    color: #fff !important;
    font-weight: 700 !important;
    font-size: 18px !important;
    padding: 16px 40px !important;
    border-radius: 2px !important;
    border: none !important;
    width: 100% !important;
    letter-spacing: 1px !important;
    display: block !important;
    text-align: center !important;
}

hr { border-top: 1px solid rgba(201,168,76,0.3) !important; }
img { border-radius: 4px !important; }
</style>
""", unsafe_allow_html=True)

WHATSAPP = "https://wa.me/5561992473134?text=Ol%C3%A1!%20Gostaria%20de%20fazer%20meu%20or%C3%A7amento."

# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  HEADER                                                                  ║
# ╚══════════════════════════════════════════════════════════════════════════╝
st.markdown(f"""
<div style="background:#0f0f0f;border-bottom:2px solid #C9A84C;padding:16px 32px;
            display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;">
  <div style="display:flex;align-items:center;gap:16px;">
    <img src="data:image/jpeg;base64,{IMG_LOGO}" alt="Logo Elitee"
         style="height:70px;width:auto;border-radius:50%;"/>
    <div>
      <div style="font-family:'Bebas Neue',sans-serif;font-size:28px;color:#C9A84C;letter-spacing:3px;">
        Instalações Elitee
      </div>
      <div style="font-size:11px;color:#666;letter-spacing:2px;text-transform:uppercase;">
        Elétrica &amp; Hidráulica Profissional
      </div>
    </div>
  </div>
  <div style="text-align:right;">
    <div style="font-size:10px;color:#666;letter-spacing:1px;text-transform:uppercase;">Ligue agora</div>
    <div style="font-family:'Bebas Neue',sans-serif;font-size:24px;color:#E8C96A;letter-spacing:1px;">
      (61) 99247-3134
    </div>
    <div style="font-size:11px;color:#555;">Atendemos DF e Entorno</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  HERO                                                                    ║
# ╚══════════════════════════════════════════════════════════════════════════╝
col_hero_txt, col_hero_img = st.columns([1, 1], gap="medium")

with col_hero_txt:
    st.markdown("""
    <div style="padding:48px 32px 32px;">
      <div style="display:inline-block;background:rgba(201,168,76,0.15);border:1px solid #C9A84C;
                  color:#C9A84C;font-size:11px;letter-spacing:3px;text-transform:uppercase;
                  padding:5px 14px;border-radius:2px;margin-bottom:20px;">
        Distrito Federal e Entorno
      </div>
      <h1 style="font-size:58px !important;line-height:1 !important;color:#f5f5f2 !important;
                 margin-bottom:8px !important;">
        Soluções Elite<br><span style="color:#C9A84C;">para seu imóvel</span>
      </h1>
      <p style="font-size:16px;color:#999;font-family:'Barlow',sans-serif;
                max-width:480px;line-height:1.8;margin-bottom:32px;">
        Referência em engenharia elétrica e hidráulica no DF.
        Segurança, qualidade e atendimento técnico com mais de 20 anos de experiência.
      </p>
      <div style="display:flex;gap:32px;padding-top:24px;border-top:1px solid #222;flex-wrap:wrap;">
        <div>
          <div style="font-family:'Bebas Neue',sans-serif;font-size:38px;color:#C9A84C;line-height:1;">20+</div>
          <div style="font-size:11px;color:#666;letter-spacing:1px;text-transform:uppercase;">Anos de Experiência</div>
        </div>
        <div>
          <div style="font-family:'Bebas Neue',sans-serif;font-size:38px;color:#C9A84C;line-height:1;">500+</div>
          <div style="font-size:11px;color:#666;letter-spacing:1px;text-transform:uppercase;">Obras Realizadas</div>
        </div>
        <div>
          <div style="font-family:'Bebas Neue',sans-serif;font-size:38px;color:#C9A84C;line-height:1;">NBR</div>
          <div style="font-size:11px;color:#666;letter-spacing:1px;text-transform:uppercase;">5410 Certificado</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

with col_hero_img:
    st.markdown(f"<div style='padding:24px 32px 0 0;'>{img_tag(IMG_DESTAQUE, 'Centro de Medição Coletiva')}</div>",
                unsafe_allow_html=True)

# ── Botão WhatsApp principal ─────────────────────────────────────────────────
st.markdown("<div style='padding:0 32px 40px;'>", unsafe_allow_html=True)
st.link_button("📲  FAÇA SEU ORÇAMENTO GRATUITO NO WHATSAPP", WHATSAPP)
st.markdown("</div>", unsafe_allow_html=True)

# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  DIFERENCIAIS                                                            ║
# ╚══════════════════════════════════════════════════════════════════════════╝
st.markdown("""
<div style="background:#0f0f0f;padding:48px 32px 0;">
  <div style="font-size:11px;color:#C9A84C;letter-spacing:4px;text-transform:uppercase;margin-bottom:8px;">
    Por que nos escolher
  </div>
  <h2 style="font-size:36px !important;margin-bottom:32px !important;">Nossos Diferenciais</h2>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3, gap="medium")
cards = [
    ("🏆", "20+ Anos", "Experiência comprovada em grandes obras prediais e residenciais no Distrito Federal."),
    ("🛡️", "Segurança", "Seguimos rigorosamente as normas NBR-5410 e todos os padrões técnicos vigentes."),
    ("✅", "Garantia", "Suporte técnico pós-serviço e compromisso total com a durabilidade das instalações."),
]
for col, (icon, title, text) in zip([c1, c2, c3], cards):
    with col:
        st.markdown(f"""
        <div style="background:#1a1a1a;border:1px solid #2a2a2a;border-top:2px solid #C9A84C;
                    padding:28px 22px;margin:0 16px 24px;min-height:160px;">
          <div style="font-size:28px;margin-bottom:14px;">{icon}</div>
          <div style="font-family:'Bebas Neue',sans-serif;font-size:22px;color:#C9A84C;
                      letter-spacing:1px;margin-bottom:8px;">{title}</div>
          <div style="font-size:14px;color:#999;line-height:1.7;font-family:'Barlow',sans-serif;">{text}</div>
        </div>
        """, unsafe_allow_html=True)

# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  ESPECIALIDADES                                                          ║
# ╚══════════════════════════════════════════════════════════════════════════╝
st.markdown("<hr style='margin:0;'/>", unsafe_allow_html=True)
st.markdown("""
<div style="padding:48px 32px 24px;">
  <div style="font-size:11px;color:#C9A84C;letter-spacing:4px;text-transform:uppercase;margin-bottom:8px;">
    O que fazemos
  </div>
  <h2 style="font-size:36px !important;margin-bottom:0 !important;">Nossas Especialidades</h2>
</div>
""", unsafe_allow_html=True)

col_e, col_h = st.columns(2, gap="medium")

with col_e:
    st.markdown(f"""
    <div style="padding:0 16px 0 32px;">
      <div style="background:#1a1a1a;border:1px solid #222;padding:28px;">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px;
                    padding-bottom:14px;border-bottom:1px solid #2a2a2a;">
          <div style="width:42px;height:42px;background:rgba(201,168,76,0.1);border:1px solid #C9A84C;
                      border-radius:2px;display:flex;align-items:center;justify-content:center;font-size:18px;">⚡</div>
          <div>
            <div style="font-size:11px;color:#C9A84C;letter-spacing:2px;text-transform:uppercase;font-family:'Barlow',sans-serif;">Área de atuação</div>
            <div style="font-family:'Bebas Neue',sans-serif;font-size:20px;color:#f5f5f2;letter-spacing:1px;">Elétrica Predial e Residencial</div>
          </div>
        </div>
        {img_tag(IMG_ELETRICA, 'Elétrica')}
        <ul style="list-style:none;padding:0;margin-top:16px;">
          <li style="font-size:14px;color:#bbb;padding:7px 0;border-bottom:1px solid #1e1e1e;display:flex;align-items:center;gap:8px;font-family:'Barlow',sans-serif;">
            <span style="width:4px;height:4px;background:#C9A84C;border-radius:50%;display:inline-block;flex-shrink:0;"></span>Instalação de Quadros de Distribuição</li>
          <li style="font-size:14px;color:#bbb;padding:7px 0;border-bottom:1px solid #1e1e1e;display:flex;align-items:center;gap:8px;font-family:'Barlow',sans-serif;">
            <span style="width:4px;height:4px;background:#C9A84C;border-radius:50%;display:inline-block;flex-shrink:0;"></span>Manutenção de Sistemas de Bombas</li>
          <li style="font-size:14px;color:#bbb;padding:7px 0;border-bottom:1px solid #1e1e1e;display:flex;align-items:center;gap:8px;font-family:'Barlow',sans-serif;">
            <span style="width:4px;height:4px;background:#C9A84C;border-radius:50%;display:inline-block;flex-shrink:0;"></span>Infraestrutura Completa para Condomínios</li>
          <li style="font-size:14px;color:#bbb;padding:7px 0;border-bottom:1px solid #1e1e1e;display:flex;align-items:center;gap:8px;font-family:'Barlow',sans-serif;">
            <span style="width:4px;height:4px;background:#C9A84C;border-radius:50%;display:inline-block;flex-shrink:0;"></span>Iluminação e Automação</li>
          <li style="font-size:14px;color:#bbb;padding:7px 0;display:flex;align-items:center;gap:8px;font-family:'Barlow',sans-serif;">
            <span style="width:4px;height:4px;background:#C9A84C;border-radius:50%;display:inline-block;flex-shrink:0;"></span>Centros de Medição Coletiva</li>
        </ul>
      </div>
    </div>
    """, unsafe_allow_html=True)

with col_h:
    st.markdown(f"""
    <div style="padding:0 32px 0 16px;">
      <div style="background:#1a1a1a;border:1px solid #222;padding:28px;">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px;
                    padding-bottom:14px;border-bottom:1px solid #2a2a2a;">
          <div style="width:42px;height:42px;background:rgba(201,168,76,0.1);border:1px solid #C9A84C;
                      border-radius:2px;display:flex;align-items:center;justify-content:center;font-size:18px;">💧</div>
          <div>
            <div style="font-size:11px;color:#C9A84C;letter-spacing:2px;text-transform:uppercase;font-family:'Barlow',sans-serif;">Área de atuação</div>
            <div style="font-family:'Bebas Neue',sans-serif;font-size:20px;color:#f5f5f2;letter-spacing:1px;">Hidráulica e Sistemas</div>
          </div>
        </div>
        {img_tag(IMG_HIDRAULICA, 'Hidráulica')}
        <ul style="list-style:none;padding:0;margin-top:16px;">
          <li style="font-size:14px;color:#bbb;padding:7px 0;border-bottom:1px solid #1e1e1e;display:flex;align-items:center;gap:8px;font-family:'Barlow',sans-serif;">
            <span style="width:4px;height:4px;background:#C9A84C;border-radius:50%;display:inline-block;flex-shrink:0;"></span>Reparo de Vazamentos Estruturais</li>
          <li style="font-size:14px;color:#bbb;padding:7px 0;border-bottom:1px solid #1e1e1e;display:flex;align-items:center;gap:8px;font-family:'Barlow',sans-serif;">
            <span style="width:4px;height:4px;background:#C9A84C;border-radius:50%;display:inline-block;flex-shrink:0;"></span>Manutenção Preventiva de Bombas</li>
          <li style="font-size:14px;color:#bbb;padding:7px 0;border-bottom:1px solid #1e1e1e;display:flex;align-items:center;gap:8px;font-family:'Barlow',sans-serif;">
            <span style="width:4px;height:4px;background:#C9A84C;border-radius:50%;display:inline-block;flex-shrink:0;"></span>Limpeza e Vedação de Reservatórios</li>
          <li style="font-size:14px;color:#bbb;padding:7px 0;border-bottom:1px solid #1e1e1e;display:flex;align-items:center;gap:8px;font-family:'Barlow',sans-serif;">
            <span style="width:4px;height:4px;background:#C9A84C;border-radius:50%;display:inline-block;flex-shrink:0;"></span>Redes de Incêndio e Recalque</li>
          <li style="font-size:14px;color:#bbb;padding:7px 0;display:flex;align-items:center;gap:8px;font-family:'Barlow',sans-serif;">
            <span style="width:4px;height:4px;background:#C9A84C;border-radius:50%;display:inline-block;flex-shrink:0;"></span>Sistemas de Bombas e Alinhamento</li>
        </ul>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  GALERIA                                                                 ║
# ╚══════════════════════════════════════════════════════════════════════════╝
st.markdown("<hr style='margin:32px 0;'/>", unsafe_allow_html=True)
st.markdown("""
<div style="padding:0 32px 24px;">
  <div style="font-size:11px;color:#C9A84C;letter-spacing:4px;text-transform:uppercase;margin-bottom:8px;">
    Nossos trabalhos
  </div>
  <h2 style="font-size:36px !important;margin-bottom:24px !important;">Galeria de Projetos</h2>
</div>
""", unsafe_allow_html=True)

g1, g2 = st.columns(2, gap="medium")
with g1:
    st.markdown(f"""
    <div style="padding:0 16px 0 32px;">
      {img_tag(IMG_DESTAQUE, 'Grandes Projetos: Infraestrutura Completa')}
      <div style="text-align:center;font-size:13px;color:#666;padding:8px 0;font-family:'Barlow',sans-serif;">
        Grandes Projetos: Infraestrutura Completa
      </div>
    </div>""", unsafe_allow_html=True)
with g2:
    st.markdown(f"""
    <div style="padding:0 32px 0 16px;">
      {img_tag(IMG_ELETRICA, 'Padrão Elitee de Organização')}
      <div style="text-align:center;font-size:13px;color:#666;padding:8px 0;font-family:'Barlow',sans-serif;">
        Padrão Elitee de Organização
      </div>
    </div>""", unsafe_allow_html=True)

# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  NORMA NBR                                                               ║
# ╚══════════════════════════════════════════════════════════════════════════╝
st.markdown("""
<div style="margin:32px 32px 24px;background:#111;border:1px solid #2a2000;
            border-left:3px solid #C9A84C;padding:20px 24px;display:flex;
            align-items:center;gap:16px;flex-wrap:wrap;">
  <div style="background:rgba(201,168,76,0.15);color:#C9A84C;
              font-family:'Bebas Neue',sans-serif;font-size:20px;letter-spacing:1px;
              padding:6px 14px;border:1px solid #C9A84C;flex-shrink:0;">NBR-5410</div>
  <div style="font-size:14px;color:#aaa;line-height:1.7;font-family:'Barlow',sans-serif;">
    <strong style="color:#f5f5f2;">Todas as instalações seguem rigorosamente as normas técnicas brasileiras.</strong>
    Garantia de conformidade, segurança e durabilidade para sua residência ou empreendimento.
  </div>
</div>
""", unsafe_allow_html=True)

# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  DICAS                                                                   ║
# ╚══════════════════════════════════════════════════════════════════════════╝
st.markdown("<hr style='margin:8px 0;'/>", unsafe_allow_html=True)
col_dica, col_dica_img = st.columns([1, 1], gap="medium")

with col_dica:
    st.markdown("""
    <div style="padding:40px 16px 40px 32px;">
      <div style="font-size:11px;color:#C9A84C;letter-spacing:4px;text-transform:uppercase;margin-bottom:8px;">
        Fique por dentro
      </div>
      <h2 style="font-size:36px !important;margin-bottom:16px !important;">💡 Dicas da Elitee</h2>
      <p style="font-size:15px;color:#aaa;line-height:1.8;font-family:'Barlow',sans-serif;">
        Prevenção é economia! Muitas vezes, uma simples revisão no quadro elétrico evita
        incêndios e pode reduzir sua conta de luz em até 20%.
      </p>
      <p style="font-size:15px;color:#aaa;line-height:1.8;font-family:'Barlow',sans-serif;margin-top:12px;">
        Não arrisque seu patrimônio com serviços improvisados.
        Contrate quem conhece o padrão do DF.
      </p>
      <div style="background:rgba(201,168,76,0.08);border-left:2px solid #C9A84C;
                  padding:12px 18px;margin-top:24px;font-size:14px;color:#E8C96A;
                  font-style:italic;font-family:'Barlow',sans-serif;">
        "Segurança elétrica não é custo — é investimento."
      </div>
    </div>
    """, unsafe_allow_html=True)

with col_dica_img:
    st.markdown(f"<div style='padding:40px 32px 40px 16px;'>{img_tag(IMG_DICAS, 'Dicas Elitee')}</div>",
                unsafe_allow_html=True)

# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  CTA                                                                     ║
# ╚══════════════════════════════════════════════════════════════════════════╝
st.markdown("""
<div style="background:#0f0f0f;border-top:2px solid #C9A84C;border-bottom:2px solid #C9A84C;
            padding:56px 32px;text-align:center;margin-top:16px;">
  <div style="font-size:11px;color:#C9A84C;letter-spacing:4px;text-transform:uppercase;margin-bottom:12px;">
    Atendimento imediato
  </div>
  <h2 style="font-size:46px !important;color:#f5f5f2 !important;margin-bottom:8px !important;">
    Faça seu Orçamento <span style="color:#C9A84C;">Gratuito</span>
  </h2>
  <p style="font-size:15px;color:#666;margin-bottom:32px;font-family:'Barlow',sans-serif;">
    Resposta rápida · Sem compromisso · Técnico especializado
  </p>
</div>
""", unsafe_allow_html=True)

col_z1, col_z2, col_z3 = st.columns([1, 2, 1])
with col_z2:
    st.link_button("📲  FALAR COM O TÉCNICO KLEBER NO WHATSAPP", WHATSAPP)
    st.markdown(f"""
    <div style="margin-top:32px;">
      {img_tag(IMG_INFORMACOES, 'Informações de Contato', 'width:100%;border-radius:8px;')}
    </div>
    <div style="display:flex;justify-content:center;gap:32px;flex-wrap:wrap;
                margin-top:16px;padding:0 0 40px;">
      <div style="font-size:13px;color:#555;font-family:'Barlow',sans-serif;">
        📍 <strong style="color:#888;">Todo o DF e Entorno</strong>
      </div>
      <div style="font-size:13px;color:#555;font-family:'Barlow',sans-serif;">
        📧 <strong style="color:#888;">instalacoes.eliteedf@gmail.com</strong>
      </div>
      <div style="font-size:13px;color:#555;font-family:'Barlow',sans-serif;">
        📱 <strong style="color:#888;">(61) 99247-3134</strong>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  RODAPÉ                                                                  ║
# ╚══════════════════════════════════════════════════════════════════════════╝
st.markdown(f"""
<div style="background:#0a0a0a;border-top:1px solid #1a1a1a;padding:24px 32px;
            display:flex;justify-content:space-between;align-items:center;
            flex-wrap:wrap;gap:12px;margin-top:16px;">
  <div style="display:flex;align-items:center;gap:12px;">
    <img src="data:image/jpeg;base64,{IMG_LOGO}" alt="Logo"
         style="height:50px;width:auto;border-radius:50%;"/>
    <div>
      <div style="font-family:'Bebas Neue',sans-serif;font-size:20px;color:#C9A84C;letter-spacing:2px;">
        Instalações Elitee
      </div>
      <div style="font-size:12px;color:#333;font-family:'Barlow',sans-serif;">
        © 2026 · Todos os direitos reservados
      </div>
    </div>
  </div>
  <div style="text-align:right;font-size:12px;color:#444;font-family:'Barlow',sans-serif;line-height:1.8;">
    Eletricista Responsável: Kleber<br>
    Atendimento: DF e Cidades do Entorno
  </div>
</div>
""", unsafe_allow_html=True)
