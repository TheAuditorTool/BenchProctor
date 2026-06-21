# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest02086():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
