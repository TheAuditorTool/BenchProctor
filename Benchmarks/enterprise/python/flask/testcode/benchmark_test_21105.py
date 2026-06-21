# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest21105():
    env_value = os.environ.get('USER_INPUT', '')
    data = ensure_str(env_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
