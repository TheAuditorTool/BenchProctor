# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest09594():
    host_value = request.headers.get('Host', '')
    attempts = globals().setdefault('_login_attempts', {})
    attempts['user'] = attempts.get('user', 0) + 1
    if auth_check('user', str(host_value)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
