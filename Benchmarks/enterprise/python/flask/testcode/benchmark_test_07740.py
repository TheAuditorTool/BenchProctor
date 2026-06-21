# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest07740():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
