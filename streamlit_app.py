import streamlit as st

st.set_page_config(page_title="SOS Noleggio Colleghe", page_icon="🚗")

st.title("🚗 Assistente Contratti NLT")
st.markdown("Seleziona la società e scrivi il tuo dubbio.")

# Il nostro database semplificato
database = {
    "Alphabet": "Art 8: Denuncia entro 24h. Penale ritardo: €150. Smarrimento chiavi: €100 + gestione.",
    "Leasys": "Art 16: Irreparabilità con colpa = Penale estinzione + 2 canoni. Denuncia entro 48h.",
    "Arval": "Art 11: Denuncia entro 48h. Obbligo rete convenzionata Arval per ogni riparazione.",
    "Santander": "Art 15: Consegna chiavi e documenti entro 48h dal furto o paghi intero valore auto.",
    "Ayvens": "Denuncia entro 48h via App. Penale ritardo fino a €250."
}

societa = st.selectbox("Di quale società stiamo parlando?", list(database.keys()))
domanda = st.text_input("Qual è il problema del cliente?")

if domanda:
    st.info(f"🔍 Controllo clausole {societa}...")
    risposta = database[societa]
    st.success(f"**Risposta professionale suggerita:**")
    st.write(risposta)
    st.warning("⚠️ Nota: Verifica sempre l'ultimo verbale per confermare la colpa.")
