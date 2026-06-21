# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest64543(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
