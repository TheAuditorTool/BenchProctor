# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session


request_state: dict[str, str] = {}

def BenchmarkTest31886():
    header_value = request.headers.get('X-Custom-Header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
