# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest14756():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
