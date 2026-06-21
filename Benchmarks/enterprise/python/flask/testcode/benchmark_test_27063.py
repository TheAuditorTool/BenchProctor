# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import os
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest27063():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
