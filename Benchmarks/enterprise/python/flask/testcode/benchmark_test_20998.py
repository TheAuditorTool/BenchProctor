# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest20998():
    env_value = os.environ.get('USER_INPUT', '')
    auth_check('user', env_value)
    return jsonify({"result": "success"})
