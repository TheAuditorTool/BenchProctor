# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest48468():
    env_value = os.environ.get('USER_INPUT', '')
    prefix = ''
    data = prefix + str(env_value)
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
