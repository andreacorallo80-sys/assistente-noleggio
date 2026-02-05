DATA = {
    "ARVAL": {
        "identità": "Arval - Gruppo BNP Paribas",
        "foro_b2b": "Firenze",
        "art_chiave": {
            "sinistri": {"art": "7 e 11", "regola": "Denuncia entro 48h. Obbligo CAI firmato.", "logica": "Se manca la firma della controparte, Arval presume la colpa del cliente e addebita tutto."},
            "estero": {"art": "18.1", "regola": "UE e Carta Verde ok. Extra-UE serve delega.", "logica": "Verificare se il paese è barrato sulla carta verde. Se sì, il cliente non deve partire senza autorizzazione scritta."},
            "recesso": {"art": "14", "regola": "Preavviso 60gg. Penale 35% canoni residui.", "logica": "Oltre alla penale, scatta il conguaglio km. Se ha fatto troppi km, la penale raddoppia nei fatti."},
            "bollo": {"art": "5", "regola": "Gestito da Arval.", "logica": "Il cliente non deve fare nulla, Arval paga e (se previsto) riaddebita in fattura."},
            "manutenzione": {"art": "8", "regola": "Solo Arval Center. Obbligo controllo livelli.", "logica": "Se il motore fonde per mancanza olio, Arval addebita l'intero costo perché è 'omessa custodia'."}
        }
    },
    "ALPHABET": {
        "identità": "Alphabet - Gruppo BMW",
        "foro_b2b": "Roma",
        "art_chiave": {
            "sinistri": {"art": "8.2", "regola": "Denuncia TASSATIVA entro 24 ore.", "logica": "Alphabet applica una penale di 150€ anche solo per un'ora di ritardo nella denuncia."},
            "documenti": {"art": "9.1", "regola": "Smarrimento libretto costa 100€ + IVA.", "logica": "È un onere amministrativo fisso, non trattabile."},
            "estero": {"art": "4.2", "regola": "Serve delega per alcuni paesi extra-UE.", "logica": "La delega Alphabet costa circa 25€ e va chiesta con largo anticipo."}
        }
    },
    "LEASYS": {
        "identità": "Leasys - Stellantis/Crédit Agricole",
        "foro_b2b": "Roma",
        "art_chiave": {
            "sinistro_totale": {"art": "16.4", "regola": "Penali pesantissime per irreparabilità con colpa.", "logica": "Il cliente paga canoni residui, penale estinzione e spesso la differenza valore a nuovo."},
            "chiavi": {"art": "15", "regola": "Furto? Servono 2 chiavi originali entro 48h.", "logica": "Se il cliente ha perso una chiave mesi fa e non ha fatto denuncia allora, oggi paga l'intera auto."}
        }
    }
}
