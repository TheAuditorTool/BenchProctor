# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest31230():
    env_value = os.environ.get('USER_INPUT', '')
    eval(str(env_value))
    return jsonify({"result": "success"})
