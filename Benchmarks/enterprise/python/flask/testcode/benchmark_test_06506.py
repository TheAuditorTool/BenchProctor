# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06506():
    cookie_value = request.cookies.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    eval(str(data))
    return jsonify({"result": "success"})
