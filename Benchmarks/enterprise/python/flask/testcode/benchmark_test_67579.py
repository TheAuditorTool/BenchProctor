# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest67579():
    env_value = os.environ.get('USER_INPUT', '')
    if not str(env_value).isdigit():
        raise ValueError('invalid input: ' + str(env_value))
    return jsonify({"result": "success"})
