# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest36288():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
