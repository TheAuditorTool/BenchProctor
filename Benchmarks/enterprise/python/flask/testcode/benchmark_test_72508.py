# SPDX-License-Identifier: Apache-2.0
import random
import os
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest72508():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
