# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest18093():
    ua_value = request.headers.get('User-Agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
