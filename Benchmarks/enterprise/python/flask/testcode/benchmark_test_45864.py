# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest45864():
    field_value = request.form.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return jsonify({'secret': str(secret)}), 200
