def insert_data(conn, data):
    try:
        print(f"📥 Dados recebidos: {data}")
        cursor = conn.cursor()

        query = """
        INSERT INTO Registros (data, ordem_producao, quantidade, artigo, cor, peso, conferente, turno)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """

        values = (
            data['data'],
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
        print(f"❌ Erro ao inserir no banco: {e}")
        return False
