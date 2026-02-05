 import streamlit as st
from database import DATA

st.set_page_config(page_title="AI NLT Advisor PRO", layout="centered")

st.title("🤖 AI Assistente Contratti NLT")
st.markdown("Chiedi aiuto per gestire i clienti e le clausole delle 5 società principali.")

# Selezione Contesto
col1, col2 = st.columns(2)
with col1:
    soc = st.selectbox("Società:", sorted(list(DATA.keys())))
with col2:
    tipo = st.selectbox("Tipo Cliente:", sorted(list(DATA[soc].keys())))

# Input Discorsivo
domanda = st.text_input("Cosa ti sta chiedendo il cliente o la collega? (es: 'Può andare all'estero?')")

if domanda:
    q = domanda.lower()
    st.divider()
    
    # Motore di ragionamento (Mappatura Intenti)
    intento = None
    if any(x in q for x in ["estero", "svizzera", "viaggio", "fuori"]): intento = "estero"
    elif any(x in q for x in ["incidente", "sinistro", "cai", "danno", "colpa"]): intento = "sinistri"
    elif any(x in q for x in ["tagliando", "officina", "olio", "manutenz"]): intento = "manutenzione"
    elif any(x in q for x in ["chiudere", "recedere", "penale", "ripensamento"]): intento = "recesso"
    elif any(x in q for x in ["avvocato", "foro", "tribunale", "causa"]): intento = "foro"
    elif any(x in q for x in ["macchina", "cortesia", "sostitutiva"]): intento = "sostitutiva"
    elif any(x in q for x in ["restituire", "consegnare", "chiavi", "fine"]): intento = "restituzione"

    # Ricerca nel Database
    regole = DATA[soc][tipo]
    risorsa = None
    
    # Trova la regola corrispondente o affine
    for k in regole.keys():
        if intento and intento in k:
            risorsa = regole[k]
            break

    if risorsa:
        with st.chat_message("assistant"):
            st.markdown(f"### 🧐 Ragionamento per la Collega")
            st.write(f"In base al contratto **{soc}**, stiamo parlando dell'**Articolo {risorsa['art']}**.")
            
            st.info(f"**Cosa dice il contratto:** {risorsa['testo']}")
            
            st.markdown("### 🗣️ Suggerimento per il Cliente")
            st.success(risorsa['consiglio'])
            
            if soc == "ARVAL" and "foro" in q and tipo == "Aziende (B2B)":
                st.warning("Nota: Ricordati che l'Art. 25 stabilisce Firenze come foro esclusivo. È un'arma forte contro gli avvocati.")
    else:
        st.warning("Non trovo un articolo specifico per questa domanda. Prova con parole più dirette (es: 'sinistro', 'estero', 'foro', 'recesso').")

st.divider()
st.caption("Sistema basato sui PDF ufficiali 2026. Consultare sempre le CGC cartacee per i dettagli dell'ordine.")
