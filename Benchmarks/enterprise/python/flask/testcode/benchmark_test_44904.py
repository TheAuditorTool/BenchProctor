# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest44904(path_param):
    path_value = path_param
    attempts = globals().setdefault('_login_attempts', {})
    attempts['user'] = attempts.get('user', 0) + 1
    if auth_check('user', str(path_value)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
