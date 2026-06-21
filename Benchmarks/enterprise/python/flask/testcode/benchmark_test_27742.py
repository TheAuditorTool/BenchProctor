# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest27742():
    cookie_value = request.cookies.get('session_token', '')
    data = relay_value(cookie_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})
