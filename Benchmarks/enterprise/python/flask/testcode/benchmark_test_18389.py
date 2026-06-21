# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest18389():
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
