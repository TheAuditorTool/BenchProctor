# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


def relay_value(value):
    return value

def BenchmarkTest02170():
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
