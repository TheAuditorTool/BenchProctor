# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest59672():
    cookie_value = request.cookies.get('session_token', '')
    if not auth_check(session.get('user', ''), str(cookie_value)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
