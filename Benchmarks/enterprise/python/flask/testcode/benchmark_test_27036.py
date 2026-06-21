# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest27036():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        int(str(env_value))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
