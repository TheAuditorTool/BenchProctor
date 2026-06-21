# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest36753():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
