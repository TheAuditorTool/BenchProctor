# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28453():
    cookie_value = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
