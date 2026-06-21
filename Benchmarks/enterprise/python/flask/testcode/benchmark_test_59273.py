# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest59273():
    header_value = request.headers.get('X-Custom-Header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
