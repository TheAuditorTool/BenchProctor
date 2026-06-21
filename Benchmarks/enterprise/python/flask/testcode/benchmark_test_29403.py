# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from flask import session
from app_runtime import auth_check


request_state: dict[str, str] = {}

def BenchmarkTest29403():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
