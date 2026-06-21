# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest62454():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        exec(str(data))
    return jsonify({"result": "success"})
