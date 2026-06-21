# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest47288():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
