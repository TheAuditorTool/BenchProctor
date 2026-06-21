# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import os


def relay_value(value):
    return value

def BenchmarkTest63856():
    host_value = request.headers.get('Host', '')
    data = relay_value(host_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
