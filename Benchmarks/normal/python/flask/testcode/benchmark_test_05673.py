# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest05673():
    auth_header = request.headers.get('Authorization', '')
    data = ensure_str(auth_header)
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    if result is None:
        return jsonify({'error': 'not found'}), 404
    value = result['name']
    return jsonify({'name': str(value)}), 200
