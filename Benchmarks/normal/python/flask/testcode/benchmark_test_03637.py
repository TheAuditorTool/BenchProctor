# SPDX-License-Identifier: Apache-2.0
import requests
import re
import os
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest03637():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    _resp = requests.get(str(processed))
    exec(_resp.text)
    return jsonify({"result": "success"})
