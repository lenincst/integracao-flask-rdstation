from flask import request, jsonify
from app import app

@app.route('/rdstation_webhook', methods=['POST'])
def rdstation_webhook():
    data = request.get_json()  # Obtém os dados da solicitação como um dicionário Python
    if data and 'leads' in data:
        lead = data['leads'][0]  # Assume que sempre haverá pelo menos um lead
        name = lead.get('name')
        email = lead.get('email')
        phone = lead.get('mobile_phone')
        created_at = lead.get('created_at')
        return jsonify({"name": name, "email": email, "phone": phone, "created_at": created_at}), 200
    else:
        return jsonify({"message": "Dados inválidos"}), 400
