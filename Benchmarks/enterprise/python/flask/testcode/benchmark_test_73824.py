# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest73824():
    env_value = os.environ.get('USER_INPUT', '')
    data = normalise_input(env_value)
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        return jsonify({'error': 'privilege drop failed'}), 500
    return jsonify({"result": "success"})
