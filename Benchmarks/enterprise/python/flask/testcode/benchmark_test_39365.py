# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39365():
    cookie_value = request.cookies.get('session_token', '')
    prefix = ''
    data = prefix + str(cookie_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
