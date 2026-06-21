# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest00609():
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
