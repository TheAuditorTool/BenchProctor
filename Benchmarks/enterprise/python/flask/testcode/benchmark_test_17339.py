# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest17339():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
