# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest07532():
    ua_value = request.headers.get('User-Agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    value = result['name']
    return jsonify({'name': str(value)}), 200
