# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from flask import session
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest43893():
    field_value = request.form.get('field', '')
    data = FormData(payload=field_value).payload
    if data != session.get('csrf_token'):
        return jsonify({'error': 'CSRF token mismatch'}), 403
    db.execute('UPDATE users SET name = ?', (str(data),))
    return jsonify({"result": "success"})
