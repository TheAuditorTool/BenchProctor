# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79046():
    cookie_value = request.cookies.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
