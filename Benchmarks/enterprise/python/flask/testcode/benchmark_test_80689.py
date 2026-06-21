# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
import os
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest80689():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
