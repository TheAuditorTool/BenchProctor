# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest09718():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    exec(str(data))
    return jsonify({"result": "success"})
