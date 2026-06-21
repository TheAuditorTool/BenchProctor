# SPDX-License-Identifier: Apache-2.0
import re
import os
from flask import jsonify


def relay_value(value):
    return value

def BenchmarkTest53716():
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(processed)}
