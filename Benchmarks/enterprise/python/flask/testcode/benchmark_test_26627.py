# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest26627():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    os.remove(str(data))
    return jsonify({"result": "success"})
