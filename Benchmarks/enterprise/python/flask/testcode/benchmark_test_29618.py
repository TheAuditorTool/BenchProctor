# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest29618():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    auth_check('user', data)
    return jsonify({"result": "success"})
