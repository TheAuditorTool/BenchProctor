# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest67615(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    processed = data[:64]
    if str(processed) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
