# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest56289(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
