# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59087():
    cookie_value = request.cookies.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
