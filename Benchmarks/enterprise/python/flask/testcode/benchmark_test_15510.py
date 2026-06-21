# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


request_state: dict[str, str] = {}

def BenchmarkTest15510():
    ua_value = request.headers.get('User-Agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
