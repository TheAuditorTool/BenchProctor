# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24244():
    cookie_value = request.cookies.get('session_token', '')
    prefix = ''
    data = prefix + str(cookie_value)
    eval(str(data))
    return jsonify({"result": "success"})
