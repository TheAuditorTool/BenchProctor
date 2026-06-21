# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest44917():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
