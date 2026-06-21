# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56363():
    cookie_value = request.cookies.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
