# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22183():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
