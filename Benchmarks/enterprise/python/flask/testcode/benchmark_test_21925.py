# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


request_state: dict[str, str] = {}

def BenchmarkTest21925():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
