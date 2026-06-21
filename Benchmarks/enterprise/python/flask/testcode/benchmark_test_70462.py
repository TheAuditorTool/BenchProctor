# SPDX-License-Identifier: Apache-2.0
from flask import session
import base64
from flask import request, jsonify


def BenchmarkTest70462():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    session['data'] = str(data)
    return jsonify({"result": "success"})
