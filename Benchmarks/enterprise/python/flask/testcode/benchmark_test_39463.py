# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39463():
    cookie_value = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
