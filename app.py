from flask import Flask, jsonify, request
from flask_cors import CORS
from server import create_connection
from insert import insert_data

app = Flask(__name__)
CORS(app)

# Estabelece a conexão com o banco de dados
conn = create_connection()

API_TOKEN = "MYMdxnidNv88wkuojg4m62kquXHtaWgJ"

# Teste de conexão
if conn:
    print('Conexão com o banco de dados estabelecida com sucesso.')
else:
    print('Falha ao estabelecer conexão com o banco de dados.')

# Rota inicial
@app.route('/', methods=['GET'])
def home():
    return "API Stik - Desenvolvido por João Paulo Bezerra"

# Rota para registrar dados
@app.route('/registrar', methods=['POST'])
def registrar():
    auth = request.headers.get("Authorization")
    print("🔍 Header Authorization recebido:", auth)
    if not auth or auth != f"Bearer {API_TOKEN}":
        return jsonify({'success': False, 'message': 'Não autorizado'}), 401

    data = request.get_json()
    print('📥 Dados recebidos:', data)

    if not data:
        return jsonify({'success': False, 'message': 'Nenhum dado recebido'}), 400

    success = insert_data(conn, data)
    if success:
        return jsonify({'success': True, 'message': 'Registro inserido com sucesso'})
    else:
        return jsonify({'success': False, 'message': 'Erro ao inserir registro'}), 500

if __name__ == '__main__':
    # Inicia o Flask
    app.run(host='0.0.0.0', port=5000, debug=False)
