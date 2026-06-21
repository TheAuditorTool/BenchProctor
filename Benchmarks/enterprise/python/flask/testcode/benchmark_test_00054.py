# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest00054():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
