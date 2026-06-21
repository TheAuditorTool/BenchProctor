# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest45287(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
