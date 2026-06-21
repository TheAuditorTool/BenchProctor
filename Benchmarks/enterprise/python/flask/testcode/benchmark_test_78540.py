# SPDX-License-Identifier: Apache-2.0
from flask import session
import base64
from flask import request, jsonify


def BenchmarkTest78540():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(data)
    return jsonify({"result": "success"})
