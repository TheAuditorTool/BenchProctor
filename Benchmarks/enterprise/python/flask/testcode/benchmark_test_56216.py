# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest56216():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
