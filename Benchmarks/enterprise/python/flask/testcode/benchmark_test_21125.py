# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest21125():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
