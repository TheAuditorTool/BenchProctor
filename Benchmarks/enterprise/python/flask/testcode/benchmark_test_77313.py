# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77313():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
