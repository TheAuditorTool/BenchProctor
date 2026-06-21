# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest67571():
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
