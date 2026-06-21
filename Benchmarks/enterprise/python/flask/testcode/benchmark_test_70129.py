# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


request_state: dict[str, str] = {}

def BenchmarkTest70129(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    attempts = globals().setdefault('_login_attempts', {})
    attempts['user'] = attempts.get('user', 0) + 1
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
