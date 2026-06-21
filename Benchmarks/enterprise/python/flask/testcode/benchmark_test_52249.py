# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52249():
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    int(str(data))
    return jsonify({"result": "success"})
