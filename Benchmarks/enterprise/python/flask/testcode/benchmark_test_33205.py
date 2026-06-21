# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33205():
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    eval(str(data))
    return jsonify({"result": "success"})
