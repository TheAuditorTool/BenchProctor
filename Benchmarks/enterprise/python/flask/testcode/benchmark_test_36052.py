# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest36052():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
