# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import time


request_state: dict[str, str] = {}

def BenchmarkTest03662():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    return jsonify({"result": "success"})
