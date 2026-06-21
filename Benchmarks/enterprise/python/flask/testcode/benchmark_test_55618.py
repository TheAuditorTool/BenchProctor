# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest55618(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
