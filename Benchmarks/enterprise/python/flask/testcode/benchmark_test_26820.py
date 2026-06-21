# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest26820():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    auth_check('user', data)
    return jsonify({"result": "success"})
