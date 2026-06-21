# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest69956():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
