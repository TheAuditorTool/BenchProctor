# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest18170():
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
