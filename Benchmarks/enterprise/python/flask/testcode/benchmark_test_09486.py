# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest09486():
    env_value = os.environ.get('USER_INPUT', '')
    prefix = ''
    data = prefix + str(env_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
