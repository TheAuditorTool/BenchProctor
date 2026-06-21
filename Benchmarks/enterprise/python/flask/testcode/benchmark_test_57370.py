# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest57370():
    cookie_value = request.cookies.get('session_token', '')
    data = '{}'.format(cookie_value)
    eval(str(data))
    return jsonify({"result": "success"})
