# SPDX-License-Identifier: Apache-2.0
import re
import os
from flask import jsonify
from flask import redirect
import urllib.parse


request_state: dict[str, str] = {}

def BenchmarkTest75072():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
