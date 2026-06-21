# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest81257():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
