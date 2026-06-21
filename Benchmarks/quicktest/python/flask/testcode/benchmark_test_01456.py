# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest01456():
    raw_body = request.get_data(as_text=True)
    data = relay_value(raw_body)
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    if result is None:
        return jsonify({'error': 'not found'}), 404
    value = result['name']
    return jsonify({'name': str(value)}), 200
