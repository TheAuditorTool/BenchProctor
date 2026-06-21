# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest38539():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
