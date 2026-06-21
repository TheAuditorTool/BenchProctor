# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest09522():
    host_value = request.headers.get('Host', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
