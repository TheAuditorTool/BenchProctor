# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest32042():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
