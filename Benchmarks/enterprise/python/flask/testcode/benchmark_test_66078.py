# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import os
from flask import jsonify
import time


request_state: dict[str, str] = {}

def BenchmarkTest66078():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        return redirect(str(data))
    return jsonify({"result": "success"})
