# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40451():
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
