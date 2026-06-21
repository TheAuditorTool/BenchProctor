# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest31570():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    int(str(data))
    return jsonify({"result": "success"})
