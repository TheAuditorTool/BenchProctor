# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest04268(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    return jsonify({'error': 'An internal error occurred'}), 500
