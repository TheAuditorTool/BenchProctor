# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest70897():
    origin_value = request.headers.get('Origin', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
