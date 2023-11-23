import psycopg2
from psycopg2 import sql

def create_connection(database_url):
    try:
        connection = psycopg2.connect(database_url)
        return connection
    except Exception as e:
        raise Exception(f"Error connecting to the database: {e}")

def execute_query(connection, query, params=None):
    try:
        cursor = connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    except Exception as e:
        raise Exception(f"Error executing query: {e}")
    finally:
        connection.close()
