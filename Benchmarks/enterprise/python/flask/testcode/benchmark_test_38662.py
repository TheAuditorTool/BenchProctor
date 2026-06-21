# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest38662():
    cookie_value = request.cookies.get('session_token', '')
    data = relay_value(cookie_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    session['data'] = str(processed)
    return jsonify({"result": "success"})
