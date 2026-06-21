# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest06783():
    xml_value = request.get_data(as_text=True)
    data = ensure_str(xml_value)
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    value = result['name']
    return jsonify({'name': str(value)}), 200
