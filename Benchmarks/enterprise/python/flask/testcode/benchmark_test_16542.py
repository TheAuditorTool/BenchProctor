# SPDX-License-Identifier: Apache-2.0
import secrets
import os
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest16542():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
