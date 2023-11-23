import pandas as pd
from db_connection import connect_to_db, close_connection, cx_Oracle
 
def create_view_and_export_to_excel(username, password, dsn, excel_filename):
    connection = connect_to_db(username, password, dsn)
    if connection:
        try:
            cursor = connection.cursor()
            # Crea la vista nel database
            create_view_query = """
                CREATE VIEW VistaManipolazioneDati AS
                SELECT
                    AE.ID AS APPARECCHIATURAID,
                    'Modello: ' || AE.NOMEMODELLO || ' (ID: ' || AE.ID || ')' AS DESCRIZIONEMODELLO,
                    AE.NUMEROSERIE AS NUMEROSERIE,
                    TO_CHAR(AE.DATAPRODUZIONE, 'DD/MM/YYYY') AS DATAPRODUZIONEFORMATTATA,
                    UPPER(AE.REPARTO) AS REPARTOMAIUSCOLO,
                    'Fornitore: ' || AE.FORNITORE || ', Acquisto: ' || TO_CHAR(AE.DATAACQUISTO, 'DD/MM/YYYY') AS DETTAGLIACQUISTO,
                    NVL(AE.CLIENTE, 'NESSUN CLIENTE') AS CLIENTEODEFAULT,
                    TRUNC(AE.GARANZIASCADENZA) - TRUNC(SYSDATE) AS GIORNIRIMANENTIGARANZIA,
                    UPPER(AE.STATOPRODUZIONE) AS STATOPRODUZIONEMAIUSCOLO,
                    'Dimensioni: ' || AE.DIMENSIONI || ', Peso: ' || AE.PESO || ' kg' AS DESCRIZIONEDIMENSIONIPESO
                FROM APPARECCHIATUREELETTRONICHE AE
            """
            cursor.execute(create_view_query)
            # Esegui la query sulla vista
            select_query = "SELECT * FROM VISTAMANIPOLAZIONEDATI"
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
    username = "system"
    password = "oirad1993"
    dsn = "localhost:1521/XEPDB1"

 
    excel_filename = "output.xlsx"
 
    create_view_and_export_to_excel(username, password, dsn, excel_filename)