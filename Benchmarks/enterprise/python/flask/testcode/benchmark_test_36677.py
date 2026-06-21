# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest36677():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
