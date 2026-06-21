# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22062():
    cookie_value = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
