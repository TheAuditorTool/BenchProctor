# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest08316():
    header_value = request.headers.get('X-Custom-Header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    if result is None:
        return jsonify({'error': 'not found'}), 404
    value = result['name']
    return jsonify({'name': str(value)}), 200
