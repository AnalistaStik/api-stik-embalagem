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
        # Fallback para valores padrão caso variáveis não estejam definidas no ambiente
        host = os.environ.get("PGHOST", "postgres.railway.internal")
        port = os.environ.get("PGPORT", "5432")
        dbname = os.environ.get("PGDATABASE", "railway")
        user = os.environ.get("PGUSER", "postgres")
        password = os.environ.get("PGPASSWORD", "Dg9vXr34!pKwZtM7")  # ⚠️ Substitua aqui pela sua senha real, se necessário

        print("🔍 Conectando com variáveis:")
        print("HOST:", host)
        print("PORT:", port)
        print("DB:", dbname)
        print("USER:", user)
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
    except psycopg2.Error as e:
        print("❌ ERRO AO CONECTAR AO POSTGRESQL:")
        print(f'{str(e)}')
        return None
