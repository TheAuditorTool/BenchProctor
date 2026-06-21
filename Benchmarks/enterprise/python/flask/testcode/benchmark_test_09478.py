# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest09478():
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
