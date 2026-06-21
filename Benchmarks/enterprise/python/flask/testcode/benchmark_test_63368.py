# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest63368(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
