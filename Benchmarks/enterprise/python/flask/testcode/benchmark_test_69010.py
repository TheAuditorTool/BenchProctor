# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


request_state: dict[str, str] = {}

def BenchmarkTest69010():
    auth_header = request.headers.get('Authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
