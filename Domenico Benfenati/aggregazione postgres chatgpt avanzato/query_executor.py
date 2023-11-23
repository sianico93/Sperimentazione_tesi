from db_connector import create_connection, execute_query

def run_aggregation_query(database_url):
    try:
        connection = create_connection(database_url)

        query = """
            SELECT 
                ae.tipoprodotto,
                EXTRACT(YEAR FROM ae.dataproduzione) AS annoproduzione,
                SUM(OCTET_LENGTH(ae.manualeutente)) AS dimensionetotalemanuali
            FROM apparecchiatureelettroniche ae
            GROUP BY ae.tipoprodotto, EXTRACT(YEAR FROM ae.dataproduzione);
        """

        result = execute_query(connection, query)

        return result
    except Exception as e:
        raise Exception(f"Error running aggregation query: {e}")
