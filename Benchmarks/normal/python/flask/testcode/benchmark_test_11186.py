# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest11186():
    env_value = os.environ.get('USER_INPUT', '')
    os.setuid(int(str(env_value)) if str(env_value).isdigit() else 0)
    return jsonify({"result": "success"})
