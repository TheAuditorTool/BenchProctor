# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest37978():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
