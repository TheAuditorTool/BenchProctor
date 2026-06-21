# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest73832():
    cookie_value = request.cookies.get('session_token', '')
    if len(str(cookie_value)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
