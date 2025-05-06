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
        host = os.environ.get("PGHOST", "localhost")
        port = os.environ.get("PGPORT", "19369")
        dbname = os.environ.get("PGDATABASE", "railway")
        user = os.environ.get("PGUSER", "postgres")
        password = os.environ.get("PGPASSWORD", "")

        print("🔍 Conectando ao PostgreSQL:")
        print(f"HOST: {host}")
        print(f"PORT: {port}")
        print(f"DB: {dbname}")
        print(f"USER: {user}")
        print("PWD: [oculto por segurança]")

        conn = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password
        )
        print("✅ Conexão estabelecida com sucesso.")
        return conn

    except Exception as e:
        import traceback
        print("❌ ERRO AO CONECTAR AO POSTGRESQL:")
        traceback.print_exc()
        return None


