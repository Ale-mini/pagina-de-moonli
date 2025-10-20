# backend.py
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import re

app = Flask(__name__, static_folder='.')
CORS(app)

# Lista de códigos válidos (puedes editarla o conectar a una base de datos)
CODIGOS_VALIDOS = {"123456", "654321", "111222", "222333"}

@app.route('/')
def index():
    return send_from_directory('.', 'emisoras_login.html')

@app.route('metricas')
def metricas():
    return send_from_directory('.', 'panel_metricas.html')

@app.route('/validar', methods=['POST'])
def validar_codigo():
    data = request.get_json()
    codigo = data.get('codigo', '')

    if not re.fullmatch(r'\d{6}', codigo):
        return jsonify({"ok": False, "msg": "El código debe tener 6 dígitos numéricos."}), 400

    if codigo in CODIGOS_VALIDOS:
        return jsonify({"ok": True, "msg": "Acceso concedido. Bienvenido.", "redirect": "/metricas"})
    else:
        return jsonify({"ok": False, "msg": "Código inválido o no autorizado."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)





