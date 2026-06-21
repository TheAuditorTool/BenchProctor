# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65226():
    cookie_value = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
