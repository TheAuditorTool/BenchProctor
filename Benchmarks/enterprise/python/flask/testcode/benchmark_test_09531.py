# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


request_state: dict[str, str] = {}

def BenchmarkTest09531():
    secret_value = 'config_secret_test_abc123'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    auth_check('user', data)
    return jsonify({"result": "success"})
