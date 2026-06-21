# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest13308():
    env_value = os.environ.get('USER_INPUT', '')
    attempts = globals().setdefault('_login_attempts', {})
    attempts['user'] = attempts.get('user', 0) + 1
    if auth_check('user', str(env_value)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
