# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import db


def BenchmarkTest03911():
    header_value = request.headers.get('X-Custom-Header', '')
    if header_value != session.get('csrf_token'):
        return jsonify({'error': 'CSRF token mismatch'}), 403
    db.execute('UPDATE users SET name = ?', (str(header_value),))
    return jsonify({"result": "success"})
