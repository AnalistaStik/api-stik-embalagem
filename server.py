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

import pymssql

def create_connection():
    try:
        return pymssql.connect(
            server='168.190.30.18',
            user='sa',
            password='Stik0123',
            database='PMP'
        )
    except Exception as e:
        print(f'Erro na conexão: {e}')
        return None



