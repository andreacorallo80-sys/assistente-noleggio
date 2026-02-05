import streamlit as st
from database import DATA

st.set_page_config(page_title="AI Advisor Noleggio", layout="wide")

# Pulizia spazio iniziale per evitare IndentationError
st.markdown("""<style>div.block-container{padding-top:2rem;}</style>""", unsafe_allow_html=True)

st.title("⚖️ Assistente Operativo Contratti NLT")
st.markdown("Analisi discorsiva e ragionata per la gestione del cliente")

# Selezione Contesto
col1, col2 = st.columns(2)
with col1:
    soc = st.selectbox("Società del contratto:", sorted(list(DATA.keys())))
with col2:
    st.info(f"📍 **Focus:** {DATA[soc]['identita']} ({DATA[soc]['tipo']})")

# Chat/Domanda
domanda = st.text_input("Fai una domanda (es: 'Cosa paga per un incidente?' o 'Il foro competente?')")

if domanda:
    q = domanda.lower()
    st.divider()
    
    # Motore di interpretazione concettuale
    mappa_intenti = {
        "incidente": ["incidente", "sinistro", "botto", "paga", "torto", "danni", "kasko", "rca"],
        "estero": ["estero", "svizzera", "viaggio", "fuori", "francia", "germania", "carta verde"],
        "foro": ["foro", "tribunale", "causa", "avvocato", "competente", "legale"],
        "recesso": ["recedere", "chiudere", "penale", "ripensamento", "disdetta", "estinguere"],
        "manutenzione": ["olio", "tagliando", "meccanico", "rottura", "officina", "motore"]
    }

    intento_trovato = None
    for intento, parole in mappa_intenti.items():
        if any(p in q for p in parole):
            intento_trovato = intento
            break

    if intento_trovato and intento_trovato in DATA[soc]["concetti"]:
        res = DATA[soc]["concetti"][intento_trovato]
        
        with st.chat_message("assistant"):
            st.markdown(f"### 🧐 Ragionamento per la Collega")
            st.write(f"In base al contratto **{soc}**, questa situazione è regolata dall'**Articolo {res['art']}**.")
            
            st.markdown("---")
            st.write(f"**Logica tecnica:** {res['logica']}")
            st.warning(f"**Risposta al caso specifico:** {res['risposta']}")
            
            st.markdown("### 🗣️ Suggerimento pratico (Cosa dire al cliente)")
            st.success(res['consiglio'])
    else:
        st.warning("Capisco la domanda, ma non trovo una clausola specifica. Prova a usare parole più dirette (es: 'incidente', 'estero', 'foro', 'recesso').")

st.divider()
st.caption("Strumento professionale basato su CGC 2026. Rispetta la riservatezza delle informazioni.")
