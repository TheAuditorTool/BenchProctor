# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest22636():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    int(str(data))
    return jsonify({"result": "success"})
