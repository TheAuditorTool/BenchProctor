# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08563():
    cookie_value = request.cookies.get('session_token', '')
    if str(cookie_value) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
