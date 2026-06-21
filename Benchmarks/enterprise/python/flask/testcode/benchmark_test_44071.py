# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest44071():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
