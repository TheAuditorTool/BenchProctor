# SPDX-License-Identifier: Apache-2.0
from flask import session
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest44340():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})
