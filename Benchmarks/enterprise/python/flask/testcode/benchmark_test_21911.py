# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest21911():
    raw_body = request.get_data(as_text=True)
    data = default_blank(raw_body)
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    if result is None:
        return jsonify({'error': 'not found'}), 404
    value = result['name']
    return jsonify({'name': str(value)}), 200
