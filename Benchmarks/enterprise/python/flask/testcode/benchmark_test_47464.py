# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47464():
    cookie_value = request.cookies.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
