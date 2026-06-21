# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest37244():
    cookie_value = request.cookies.get('session_token', '')
    data = to_text(cookie_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})
