# SPDX-License-Identifier: Apache-2.0
import re
import os
from flask import jsonify


def relay_value(value):
    return value

def BenchmarkTest31678():
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return jsonify({"result": "success"})
