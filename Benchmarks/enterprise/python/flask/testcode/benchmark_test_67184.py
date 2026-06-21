# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest67184():
    cookie_value = request.cookies.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    int(str(data))
    return jsonify({"result": "success"})
