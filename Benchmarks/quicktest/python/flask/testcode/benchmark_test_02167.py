# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import db


def BenchmarkTest02167():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    if data != session.get('csrf_token'):
        return jsonify({'error': 'CSRF token mismatch'}), 403
    db.execute('UPDATE users SET name = ?', (str(data),))
    return jsonify({"result": "success"})
