# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session


request_state: dict[str, str] = {}

def BenchmarkTest79356():
    xml_value = request.get_data(as_text=True)
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
