# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80467():
    cookie_value = request.cookies.get('session_token', '')
    eval(str(cookie_value))
    return jsonify({"result": "success"})
