# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest61734():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
