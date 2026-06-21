# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest12080():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
