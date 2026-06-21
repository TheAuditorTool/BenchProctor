# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest07395():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
