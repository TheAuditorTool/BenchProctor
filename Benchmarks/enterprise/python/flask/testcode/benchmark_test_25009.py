# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest25009():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
