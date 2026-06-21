# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16671():
    cookie_value = request.cookies.get('session_token', '')
    size = min(int(cookie_value) if str(cookie_value).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
