# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import db


def BenchmarkTest18486():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    if json_value != session.get('csrf_token'):
        return jsonify({'error': 'CSRF token mismatch'}), 403
    db.execute('UPDATE users SET name = ?', (str(json_value),))
    return jsonify({"result": "success"})
