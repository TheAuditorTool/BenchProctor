# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest69009():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
