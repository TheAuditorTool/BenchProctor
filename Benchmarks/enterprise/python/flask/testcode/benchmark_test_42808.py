# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42808():
    cookie_value = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
