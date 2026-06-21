# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest29972(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
