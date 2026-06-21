# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest38055():
    cookie_value = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    int(str(data))
    return jsonify({"result": "success"})
