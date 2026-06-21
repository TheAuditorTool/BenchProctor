# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest16592():
    cookie_value = request.cookies.get('session_token', '')
    if auth_check('user', str(cookie_value)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
