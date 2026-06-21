# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest03383():
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
