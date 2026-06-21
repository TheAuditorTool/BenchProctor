# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


request_state: dict[str, str] = {}

def BenchmarkTest04872():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    auth_check('user', data)
    return jsonify({"result": "success"})
