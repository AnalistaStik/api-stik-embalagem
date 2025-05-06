from flask import Flask, jsonify, request
from flask_cors import CORS
from server import create_connection
from insert import insert_data
import os

app = Flask(__name__)
CORS(app)

# Token fixo da API
API_TOKEN = "MYMdxnidNv88wkuojg4m62kquXHtaWgJ"

# Conexão com o banco
conn = create_connection()
if conn:
    print('✅ Conexão com o banco de dados estabelecida com sucesso.')
else:
    print('❌ Falha ao estabelecer conexão com o banco de dados.')

# Rota GET inicial
@app.route('/', methods=['GET'])
def home():
    return "API Stik - Desenvolvido por João Paulo Bezerra"

# Rota POST de registro
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

# Execução local e em deploy
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Railway define a porta via variável
    app.run(host='0.0.0.0', port=port)
