import streamlit as st
from database import DATA

st.set_page_config(page_title="AI NLT Advisor", layout="centered")

st.title("🤖 Il tuo Assistente Legale NLT")
st.markdown("Fai una domanda come se parlassi a un collega esperto.")

# Selezione contesto
col_a, col_b = st.columns(2)
with col_a:
    soc = st.selectbox("Società:", list(DATA.keys()))
with col_b:
    cat = st.selectbox("Tipo Cliente:", list(DATA[soc].keys()))

# Domanda discorsiva
domanda = st.text_input("Esempio: 'Cosa succede se fa un incidente?' o 'Può andare all'estero?'")

if domanda:
    q = domanda.lower()
    st.divider()
    
    # Motore di ragionamento (Mappatura Intenti)
    intento = None
    if any(x in q for x in ["estero", "viaggio", "fuori", "paesi"]): intento = "estero"
    elif any(x in q for x in ["incidente", "sinistro", "cai", "botto", "danno"]): intento = "sinistri"
    elif any(x in q for x in ["tagliando", "olio", "officina", "rottura"]): intento = "tagliando"
    elif any(x in q for x in ["chiudere", "recesso", "ripensamento", "disdetta"]): intento = "recesso"
    elif any(x in q for x in ["avvocato", "foro", "tribunale", "causa"]): intento = "foro"
    elif any(x in q for x in ["distrutta", "totale", "rottamata"]): intento = "totale"
    elif any(x in q for x in ["chiavi", "rubata", "furto"]): intento = "chiavi"
    
    if intento and intento in DATA[soc][cat]:
        res = DATA[soc][cat][intento]
        
        st.subheader("🧐 Analisi dell'Assistente")
        st.write(f"Parliamo di **{soc} ({cat})**. La regola è dettata dall'**Articolo {res['art']}**.")
        
        with st.expander("Leggi il testo tecnico del contratto"):
            st.write(res['spiegazione'])
            
        st.markdown("### 🗣️ Cosa rispondere al cliente:")
        st.success(res['consiglio'])
    else:
        st.warning("Capisco la domanda, ma non trovo una clausola specifica nel database per questo caso. Prova a usare parole più dirette (es: 'sinistro', 'estero', 'penale').")

st.divider()
st.caption("Sistema basato sui PDF ufficiali 2026.")
