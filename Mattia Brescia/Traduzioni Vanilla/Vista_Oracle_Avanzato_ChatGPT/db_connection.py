import cx_Oracle
 
def connect_to_db(username, password, database_url):
    try:
        connection = cx_Oracle.connect(username, password, database_url)
        return connection
    except cx_Oracle.Error as error:
        print(f"Errore durante la connessione al database: {error}")
        return None

def close_connection(connection):
    if connection:
        connection.close()
