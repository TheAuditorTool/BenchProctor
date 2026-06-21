# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest09405():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
