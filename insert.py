# def insert_data(conn, data):
#     try:
#         print(f"📥 Dados recebidos: {data}")
#         cursor = conn.cursor()

#         query = """
#         INSERT INTO registros (data, ordem_producao, quantidade, artigo, cor, peso, conferente, turno)
#         VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#         """

#         values = (
#             data['data'],
#             data['ordem_producao'],
#             data['quantidade'],
#             data['artigo'],
#             data['cor'],
#             data['peso'],
#             data['conferente'],
#             data['turno']
#         )

#         cursor.execute(query, values)
#         conn.commit()
#         print("✅ Inserção feita com sucesso.")
#         return True
#     except Exception as e:
#         print(f"❌ Erro ao inserir no banco: {e}")
#         return False

# from datetime import datetime, date
# import traceback

# def insert_data(conn, data):
#     try:
#         print(f"📥 Dados recebidos: {data}")
#         cursor = conn.cursor()

#         query = """
#         INSERT INTO registros (data, ordem_producao, quantidade, artigo, cor, peso, conferente, turno)
#         VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#         """

#         # Garantir que a data esteja no formato correto (date)
#         data_bruta = data['data']
#         print(f"👉 data['data']: {data_bruta} ({type(data_bruta)})")

#         if isinstance(data_bruta, str):
#             #data_convertida = datetime.strptime(data_bruta, "%Y-%m-%d").date()
#             data_convertida = datetime.strptime(data_bruta, "%Y-%m-%d")
#         elif isinstance(data_bruta, datetime):
#             data_convertida = data_bruta.date()
#         elif isinstance(data_bruta, date):
#             data_convertida = data_bruta
#         else:
#             raise ValueError(f"Formato inválido para campo 'data': {data_bruta}")

#         values = (
#             data_convertida,
#             data['ordem_producao'],
#             data['quantidade'],
#             data['artigo'],
#             data['cor'],
#             data['peso'],
#             data['conferente'],
#             data['turno']
#         )

#         cursor.execute(query, values)
#         conn.commit()
#         print("✅ Inserção feita com sucesso.")
#         return True

#     except Exception as e:
#         traceback.print_exc()
#         print(f"❌ Erro ao inserir no banco: {e}")
#         return False

# import traceback

# def insert_data(conn, data):
#     try:
#         print(f"📥 Dados recebidos: {data}")
#         cursor = conn.cursor()

#         query = """
#         INSERT INTO registros (data, ordem_producao, quantidade, artigo, cor, peso, conferente, turno)
#         VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#         """

#         values = (
#             data['data'],  # ← Usa string pura 'YYYY-MM-DD' sem .date()
#             data['ordem_producao'],
#             data['quantidade'],
#             data['artigo'],
#             data['cor'],
#             data['peso'],
#             data['conferente'],
#             data['turno']
#         )

#         cursor.execute(query, values)
#         conn.commit()
#         print("✅ Inserção feita com sucesso.")
#         return True
#     except Exception as e:
#         traceback.print_exc()
#         print(f"❌ Erro ao inserir no banco: {e}")
#         return False

from datetime import datetime, timedelta
import traceback

def insert_data(conn, data):
    try:
        print(f"📥 Dados recebidos: {data}")
        cursor = conn.cursor()

        query = """
        INSERT INTO registros (data, ordem_producao, quantidade, artigo, cor, peso, conferente, turno)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Corrige o UTC forçado do PostgreSQL somando 1 dia
        data_recebida = datetime.strptime(data['data'], "%Y-%m-%d").date()
        data_corrigida = data_recebida + timedelta(days=1)

        values = (
            data_corrigida,
            data['ordem_producao'],
            data['quantidade'],
            data['artigo'],
            data['cor'],
            data['peso'],
            data['conferente'],
            data['turno']
        )

        cursor.execute(query, values)
        conn.commit()
        print("✅ Inserção feita com sucesso.")
        return True

    except Exception as e:
        traceback.print_exc()
        print(f"❌ Erro ao inserir no banco: {e}")
        return False










