# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest54079():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
