# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03864():
    cookie_value = request.cookies.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
