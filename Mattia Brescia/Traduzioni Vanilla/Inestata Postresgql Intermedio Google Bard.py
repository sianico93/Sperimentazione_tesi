import psycopg2
 
def connetti_al_database():
    """
    Connessione al database PostgreSQL.
 
    Restituisce:
        Una connessione al database.
 
    """
 
    # Informazioni di connessione al database
    host = "localhost"
    port = 5432
    database = "mio_database"
    user = "mio_utente"
    password = "mia_password"
 
    # Connessione al database
    try:
        connection = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password,
        )
    except psycopg2.Error as error:
        raise ValueError(f"Errore di connessione al database: {error}")
 
    return connection
 
 
def esegui_query(connection, query):
    """
    Esegue una query sul database PostgreSQL.
 
    Args:
        connection: Una connessione al database.
        query: La query da eseguire.
 
    Restituisce:
        Il risultato della query.
 
    """
 
    # Creazione di un cursore
    try:
        cursor = connection.cursor()
    except psycopg2.Error as error:
        raise ValueError(f"Errore di creazione del cursore: {error}")
 
    # Esecuzione della query
    try:
        cursor.execute(query)
    except psycopg2.Error as error:
        raise ValueError(f"Errore di esecuzione della query: {error}")
 
    # Recupero del risultato della query
    results = cursor.fetchall()
 
    # Chiusura del cursore
    cursor.close()
 
    return results
 
 
def query_apparecchiature_elettroniche(connection):
    """
    Esegue la query per ottenere il nome del modello delle apparecchiature elettroniche che soddisfano i criteri specificati.
 
    Args:
        connection: Una connessione al database.
 
    Restituisce:
        Una lista di nomi di modello.
 
    """
 
    # Query
    query = """
        SELECT ae_inner."nomemodello"
        FROM "apparecchiatureelettroniche" ae_inner
        WHERE (
            SELECT digest(CONCAT(ae_inner."manualeutente", ae_inner."nomemodello"), 'sha1')
            ) = (
            SELECT digest(CONCAT(ae."manualeutente", ae."nomemodello"), 'sha1')
            FROM "apparecchiatureelettroniche" ae
            WHERE ae."id" = ae_inner."id"
            )
            AND LENGTH(ae_inner."manualeutente") > 0
            AND ae_inner."id" IN (
                SELECT po."id"
                FROM "prodottiordinati" po
                WHERE po."numeroordine" IN (
                    SELECT oc."numeroordine"
                    FROM "ordiniclienti" oc
                    WHERE oc."cittaspedizione" = 'Milano'
                        AND oc."dataordine" BETWEEN '2023-01-01' AND '2023-07-31'
                )
            );
    """
 
    # Esecuzione della query
    results = esegui_query(connection, query)
 
    return results
 
 
def main():
    """
    Funzione principale.
 
    Esegue la query per ottenere il nome del modello delle apparecchiature elettroniche che soddisfano i criteri specificati.
 
    """
 
    # Connessione al database
    connection = connetti_al_database()
 
    # Esecuzione della query
    results = query_apparecchiature_elettroniche(connection)
 
    # Stampa dell'output
    print("Nomi dei modelli:")
    for result in results:
        print(result[0])
 
    # Chiusura della connessione al database
    connection.close()
 
 
if __name__ == "__main__":
    main()