# SPDX-License-Identifier: Apache-2.0
import re
import os
from flask import jsonify


def BenchmarkTest19695():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return str(processed), 200, {'Content-Type': 'text/html'}
