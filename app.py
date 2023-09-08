from flask import Flask, Response, jsonify
from pymongo import MongoClient
from bson import json_util
import json

app = Flask(__name__)

# Função para conectar ao MongoDB
def get_mongo_client():
    client = MongoClient('mongodb-container', 27017, username='root', password='luiz1993')
    return client

# Função para converter ObjectId para string
def jsonify_mongo(data):
    return json.loads(json_util.dumps(data))

@app.route('/')
def fetch_data():
    client = get_mongo_client()
    db = client['db001']
    collection = db['teste1']

    # Busca todos os documentos na collection
    data = list(collection.find({}))

    # Fechando a conexão
    client.close()

    # Retorna os dados como um JSON válido
    return jsonify(data=jsonify_mongo(data))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
