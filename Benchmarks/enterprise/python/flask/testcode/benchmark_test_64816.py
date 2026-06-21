# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64816():
    cookie_value = request.cookies.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
