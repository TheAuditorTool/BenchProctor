# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13145():
    cookie_value = request.cookies.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
