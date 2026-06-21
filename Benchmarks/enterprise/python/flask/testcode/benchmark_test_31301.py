# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest31301():
    field_value = request.form.get('field', '')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(field_value),))
    value = result['name']
    return jsonify({'name': str(value)}), 200
