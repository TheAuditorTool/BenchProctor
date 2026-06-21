# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest73222():
    field_value = request.form.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    if data != session.get('csrf_token'):
        return jsonify({'error': 'CSRF token mismatch'}), 403
    db.execute('UPDATE users SET name = ?', (str(data),))
    return jsonify({"result": "success"})
