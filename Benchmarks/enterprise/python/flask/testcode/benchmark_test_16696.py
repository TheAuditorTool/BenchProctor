# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest16696():
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    exec(str(data))
    return jsonify({"result": "success"})
