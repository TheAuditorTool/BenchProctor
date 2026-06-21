# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest31034(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
