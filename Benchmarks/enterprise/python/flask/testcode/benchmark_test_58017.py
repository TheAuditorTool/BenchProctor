# SPDX-License-Identifier: Apache-2.0
import hashlib
import os
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest58017():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
