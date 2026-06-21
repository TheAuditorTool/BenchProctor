# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest51153():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
