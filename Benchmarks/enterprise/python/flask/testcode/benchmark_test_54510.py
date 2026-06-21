# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54510():
    cookie_value = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
