# SPDX-License-Identifier: Apache-2.0
import threading
import re
import os
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest02844():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    globals()['counter'] = int(processed)
    return jsonify({"result": "success"})
