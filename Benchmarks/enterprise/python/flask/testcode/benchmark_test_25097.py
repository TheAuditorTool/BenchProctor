# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest25097():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
