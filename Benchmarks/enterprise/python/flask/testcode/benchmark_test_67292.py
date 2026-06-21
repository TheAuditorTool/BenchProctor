# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest67292():
    cookie_value = request.cookies.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
