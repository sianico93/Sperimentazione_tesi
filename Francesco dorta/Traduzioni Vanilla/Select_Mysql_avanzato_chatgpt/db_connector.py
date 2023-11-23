import mysql.connector
 
def get_database_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="oirad1993",
            database="database4test"
        )
        return connection
    except Exception as e:
        print("Errore nella connessione al database:", str(e))
        raise