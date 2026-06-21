# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest14527():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    eval(compile("os.system('echo ' + str(data))", '<sink>', 'exec'))
    return jsonify({"result": "success"})
