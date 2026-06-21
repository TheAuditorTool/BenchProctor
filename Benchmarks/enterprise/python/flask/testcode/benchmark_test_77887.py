# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest77887():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    int(str(data))
    return jsonify({"result": "success"})
