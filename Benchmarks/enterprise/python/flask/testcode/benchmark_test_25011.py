# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session


request_state: dict[str, str] = {}

def BenchmarkTest25011():
    field_value = request.form.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
