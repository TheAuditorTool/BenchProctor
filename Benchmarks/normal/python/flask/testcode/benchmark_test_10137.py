# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


request_state: dict[str, str] = {}

def BenchmarkTest10137():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    auth_check('user', data)
    return jsonify({"result": "success"})
