# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest22808():
    env_value = os.environ.get('USER_INPUT', '')
    prefix = ''
    data = prefix + str(env_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
