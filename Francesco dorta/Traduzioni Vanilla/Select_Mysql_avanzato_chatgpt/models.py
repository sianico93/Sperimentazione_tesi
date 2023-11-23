from db_connector import get_database_connection
 
class ApparecchiatureElettronicheModel:
    def get_elettroniche_by_resolution(self):
        try:
            connection = get_database_connection()
            cursor = connection.cursor(dictionary=True)
            query = ("SELECT * FROM ApparecchiatureElettroniche "
                     "WHERE CAST(SUBSTRING_INDEX(RisoluzioneSchermo, 'x', -1) AS SIGNED) > 1080 "
                     "ORDER BY DataProduzione DESC;")
            cursor.execute(query)
            results = cursor.fetchall()
            return results
        except Exception as e:
            print("Errore durante l'esecuzione della query:", str(e))
            raise
        finally:
            cursor.close()
            connection.close()