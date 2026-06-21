# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest53244():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
