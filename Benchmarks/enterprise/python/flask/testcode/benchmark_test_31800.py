# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest31800():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    eval(str(data))
    return jsonify({"result": "success"})
