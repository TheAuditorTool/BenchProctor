# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest48980():
    xml_value = request.get_data(as_text=True)
    data = to_text(xml_value)
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    if result is None:
        return jsonify({'error': 'not found'}), 404
    value = result['name']
    return jsonify({'name': str(value)}), 200
