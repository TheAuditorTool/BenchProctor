# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest67689(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
