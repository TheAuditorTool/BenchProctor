# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest67448():
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
