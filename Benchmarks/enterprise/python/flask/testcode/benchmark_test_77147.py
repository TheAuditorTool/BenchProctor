# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest77147():
    env_value = os.environ.get('USER_INPUT', '')
    data = bytearray(int(env_value) if str(env_value).isdigit() else 0)
    return jsonify({"result": "success"})
