# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest38529():
    cookie_value = request.cookies.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
