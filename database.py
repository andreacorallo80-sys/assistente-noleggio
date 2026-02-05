DATA = {
    "ARVAL": {
        "Aziende (B2B)": {
            "regole": {
                "oggetto": {"art": "1", "testo": "Locazione veicoli nuovi + RCA + Manutenzione + Soccorso.", "ragionamento": "Il contratto copre il mezzo e i servizi base. Attenzione: AdBlue e liquidi sono esclusi (Art. 12)."},
                "prezzi": {"art": "2.2", "testo": "Arval può variare il canone se passano >90gg tra ordine e consegna.", "ragionamento": "Se la fabbrica ritarda oltre 3 mesi, Arval ha il diritto legale di aggiornare il canone ai nuovi listini."},
                "consegna": {"art": "4", "testo": "Danni segnalabili entro 24h o 100km.", "ragionamento": "Oltre le 24 ore dalla consegna, ogni danno estetico è a carico del cliente. Sii ferma su questo."},
                "bollo": {"art": "5", "testo": "Pagamento a carico di Arval.", "ragionamento": "Il cliente non deve preoccuparsi del bollo, Arval lo gestisce centralmente."},
                "sinistri": {"art": "6, 7 e 11", "testo": "RCA inclusa. Denuncia entro 48h. Obbligo CAI firmato.", "ragionamento": "Senza firma della controparte o verbale, Arval addebita il 100% del danno per colpa presunta (Art. 11)."},
                "manutenzione": {"art": "8", "testo": "Solo Arval Center. Obbligo controllo livelli olio/liquidi.", "ragionamento": "Il cliente risponde dei danni da incuria. Se fonde il motore perché non ha guardato l'olio, paga tutto lui."},
                "sostitutiva": {"art": "10", "testo": "Solo per fermi > 8h lavorative e se prevista nell'ordine.", "ragionamento": "Per i tagliandi rapidi l'auto non è dovuta. Verifica sempre il flag nell'offerta originale."},
                "estero": {"art": "18.1", "testo": "UE e Carta Verde ok. Extra-UE serve delega scritta.", "ragionamento": "Se il paese è sbarrato sulla carta verde, il cliente rischia il sequestro se non ha l'autorizzazione di Arval."},
                "recesso": {"art": "14", "testo": "Penale 35% canoni residui + conguaglio chilometrico.", "ragionamento": "Oltre alla penale, scatta il ricalcolo dei km: se ne ha fatti troppi, il conguaglio sarà pesantissimo."},
                "foro": {"art": "25", "testo": "Competenza esclusiva del Foro di Firenze.", "ragionamento": "Usa questo per fermare gli avvocati: ogni causa deve essere fatta a Firenze, non nella città del cliente."},
                "restituzione": {"art": "16", "testo": "Resa con 2 chiavi e documenti. Danni fuori norma fatturati 100%.", "ragionamento": "Se mancano le chiavi o il libretto alla resa, Arval addebita i costi di ripristino a listino pieno."}
            }
        },
        "Privati (B2C)": {
            "regole": {
                "ripensamento": {"art": "52 Cod. Consumo", "testo": "Diritto di recesso entro 14gg dalla firma.", "ragionamento": "Per i privati esiste il diritto di ripensamento se il contratto è fatto fuori sede o online."},
                "foro": {"art": "66 bis", "testo": "Foro del Consumatore (residenza del cliente).", "ragionamento": "Con i privati non possiamo imporre Firenze. Dobbiamo gestire la causa nella loro città."}
            }
        }
    },
    "ALPHABET": {
        "Aziende (B2B)": {
            "regole": {
                "sinistri": {"art": "8.2", "testo": "Denuncia entro 24 ORE. Penale ritardo € 150,00.", "ragionamento": "Alphabet è rigidissima sul tempo. Anche un'ora di ritardo fa scattare la penale di 150€."},
                "foro": {"art": "16", "testo": "Foro esclusivo Roma.", "ragionamento": "La competenza legale è unicamente su Roma."}
            }
        }
    },
    "LEASYS": {
        "Aziende (B2B)": {
            "regole": {
                "sinistro_totale": {"art": "16.4", "testo": "Penale estinzione + 2 canoni + valore a nuovo (se < 6 mesi).", "ragionamento": "In caso di distruzione auto con colpa, il conto sarà di svariate migliaia di euro."},
                "foro": {"art": "26", "testo": "Foro esclusivo Roma.", "ragionamento": "Competenza territoriale: Roma."}
            }
        }
    }
}
