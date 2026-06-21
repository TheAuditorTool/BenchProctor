# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest51256():
    header_value = request.headers.get('X-Custom-Header', '')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(header_value),))
    value = result['name']
    return jsonify({'name': str(value)}), 200
