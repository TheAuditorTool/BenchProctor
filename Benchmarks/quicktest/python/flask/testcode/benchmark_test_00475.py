# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest00475():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    if data != session.get('csrf_token'):
        return jsonify({'error': 'CSRF token mismatch'}), 403
    db.execute('UPDATE users SET name = ?', (str(data),))
    return jsonify({"result": "success"})
