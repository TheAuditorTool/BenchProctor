# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest37587():
    ua_value = request.headers.get('User-Agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
