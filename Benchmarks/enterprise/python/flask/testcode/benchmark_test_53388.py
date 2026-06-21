# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest53388():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
