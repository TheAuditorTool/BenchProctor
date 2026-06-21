# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest67081():
    raw_body = request.get_data(as_text=True)
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
