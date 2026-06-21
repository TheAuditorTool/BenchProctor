# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest81339():
    cookie_value = request.cookies.get('session_token', '')
    data = ensure_str(cookie_value)
    processed = data[:64]
    session['data'] = str(processed)
    return jsonify({"result": "success"})
