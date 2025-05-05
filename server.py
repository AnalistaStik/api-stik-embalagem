# import pyodbc

# def create_connection():
#     server = '168.190.30.18'
#     database = 'PMP'
#     username = 'sa'
#     password = 'Stik0123'
    
#     # Criar a string de conexão
#     connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    
#     # Estabelecer a conexão com o banco de dados
#     try:
#         conn = pyodbc.connect(connection_string)
#         return conn
#     except pyodbc.Error as e:
#         print(f'Erro ao conectar ao banco de dados: {str(e)}')
#         return None

import psycopg2
import os

def create_connection():
    try:
        conn = psycopg2.connect(
            host=os.environ.get("PGHOST"),
            port=os.environ.get("PGPORT"),
            dbname=os.environ.get("PGDATABASE"),
            user=os.environ.get("PGUSER"),
            password=os.environ.get("PGPASSWORD")
        )
        return conn
    except psycopg2.Error as e:
        print(f'Erro ao conectar ao banco de dados PostgreSQL: {str(e)}')
        return None
