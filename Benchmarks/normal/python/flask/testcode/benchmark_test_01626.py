# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


request_state: dict[str, str] = {}

def BenchmarkTest01626():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    processed = data[:64]
    auth_check('user', processed)
    return jsonify({"result": "success"})
