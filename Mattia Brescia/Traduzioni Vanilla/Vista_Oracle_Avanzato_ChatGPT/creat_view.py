import pandas as pd
from db_connection import connect_to_db, close_connection
 
def create_view_and_export_to_excel(username, password, database_url, excel_filename):
    connection = connect_to_db(username, password, database_url)
    if connection:
        try:
            cursor = connection.cursor()
            # Crea la vista nel database
            create_view_query = """
                CREATE VIEW VistaManipolazioneDati AS
                SELECT
                    ae.ID AS ApparecchiaturaID,
                    CONCAT('Modello: ', ae.NomeModello, ' (ID: ', ae.ID, ')') AS DescrizioneModello,
                    ae.NumeroSerie AS NumeroSerie,
                    TO_CHAR(ae.DataProduzione, 'DD/MM/YYYY') AS DataProduzioneFormattata,
                    UPPER(ae.Reparto) AS RepartoMaiuscolo,
                    CONCAT('Fornitore: ', ae.Fornitore, ', Acquisto: ', TO_CHAR(ae.DataAcquisto, 'DD/MM/YYYY')) AS DettagliAcquisto,
                    NVL(ae.Cliente, 'Nessun cliente') AS ClienteODefault,
                    TRUNC(ae.GaranziaScadenza) - TRUNC(SYSDATE) AS GiorniRimanentiGaranzia,
                    UPPER(ae.StatoProduzione) AS StatoProduzioneMaiuscolo,
                    CONCAT('Dimensioni: ', ae.Dimensioni, ', Peso: ', ae.Peso, ' kg') AS DescrizioneDimensioniPeso
                FROM ApparecchiatureElettroniche ae;
            """
            cursor.execute(create_view_query)
            # Esegui la query sulla vista
            select_query = "SELECT * FROM VistaManipolazioneDati"
            cursor.execute(select_query)
            # Ottieni i dati
            data = cursor.fetchall()
            # Crea un DataFrame pandas
            df = pd.DataFrame(data, columns=[col[0] for col in cursor.description])
            # Esporta i dati in un file Excel
            df.to_excel(excel_filename, index=False)
            print(f"Risultati esportati in {excel_filename}")
        except cx_Oracle.Error as error:
            print(f"Errore durante l'esecuzione della query: {error}")
        finally:
            cursor.close()
            close_connection(connection)
 
# Esempio di utilizzo
if __name__ == "__main__":
    username = "your_username"
    password = "your_password"
    database_url = "your_database_url"
    excel_filename = "output.xlsx"
    create_view_and_export_to_excel(username, password, database_url, excel_filename)