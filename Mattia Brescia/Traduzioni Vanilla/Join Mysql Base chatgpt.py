import mysql.connector

# Definizione delle credenziali di connessione al database MySQL
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "oirad1993",
    "database": "database4test"
}

# Creazione di una connessione al database
conn = mysql.connector.connect(**db_config)

try:
    # Creazione di un cursore per eseguire query SQL
    cursor = conn.cursor()

    # Definizione della query SQL
    query = """
    SELECT 
        po.ID AS ProdottoOrdinatoID,
        po.NumeroOrdine,
        po.NomeModello,
        po.Quantita,
        po.PrezzoUnitario AS PrezzoUnitarioProdotto,
        po.Valuta AS ValutaProdotto,
        po.DataAggiunta,
        po.DataConsegnaPrevista,
        po.StatoProdotto,
        po.NumeroRMA,
        po.Note AS NoteProdotto,
        ae.NomeModello AS NomeModelloApparecchiatura,
        ae.NumeroSerie,
        ae.DataProduzione,
        ae.Reparto,
        ae.Fornitore AS FornitoreApparecchiatura,
        ae.DataAcquisto,
        ae.Cliente,
        ae.RepartoAssistenza,
        ae.DataUltimaManutenzione,
        ae.GaranziaScadenza,
        ae.DescrizioneProblema,
        ae.ComponenteDifettoso,
        ae.TecnicoAssistenza,
        ae.Note AS NoteApparecchiatura,
        oc.NumeroOrdine AS NumeroOrdineCliente,
        oc.DataOrdine,
        oc.Cliente AS ClienteOrdine,
        oc.IndirizzoSpedizione,
        oc.CittaSpedizione,
        oc.CAPSpedizione,
        oc.ProvinciaSpedizione,
        oc.NazioneSpedizione,
        oc.MetodoPagamento,
        oc.StatoPagamento,
        oc.DataPagamento,
        oc.MetodoSpedizione,
        oc.DataSpedizione,
        oc.StatoSpedizione,
        oc.DataConsegna,
        oc.TotaleOrdine,
        oc.Valuta AS ValutaOrdine,
        oc.NumeroFattura,
        oc.CodicePromozionale,
        oc.Note AS NoteOrdine
    FROM ProdottiOrdinati po
    JOIN ApparecchiatureElettroniche ae ON po.NomeModello = ae.NomeModello
    JOIN OrdiniClienti oc ON po.NumeroOrdine = oc.NumeroOrdine
    WHERE po.DataAggiunta BETWEEN '2022-01-01' AND '2023-06-30'
        AND ae.DataProduzione <= '2023-06-30'
        AND oc.DataOrdine >= '2022-01-01';
    """

    # Esecuzione della query SQL
    cursor.execute(query)

    # Estrazione dei risultati
    results = cursor.fetchall()

    # Stampa dei risultati o elaborazione ulteriore
    for row in results:
        print(row)

finally:
    # Chiusura del cursore e della connessione
    cursor.close()
    conn.close()
