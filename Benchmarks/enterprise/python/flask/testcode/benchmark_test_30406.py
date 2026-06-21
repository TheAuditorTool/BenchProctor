# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30406():
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
