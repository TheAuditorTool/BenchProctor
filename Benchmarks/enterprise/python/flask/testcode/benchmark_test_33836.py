# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest33836():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
