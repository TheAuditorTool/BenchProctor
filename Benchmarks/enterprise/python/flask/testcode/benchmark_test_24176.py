# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest24176():
    header_value = request.headers.get('X-Custom-Header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
