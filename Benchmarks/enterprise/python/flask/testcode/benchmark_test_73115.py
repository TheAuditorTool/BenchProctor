# SPDX-License-Identifier: Apache-2.0
from flask import session
import os
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest73115():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    session['data'] = str(data)
    return jsonify({"result": "success"})
