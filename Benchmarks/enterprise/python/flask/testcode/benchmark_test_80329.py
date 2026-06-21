# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80329():
    cookie_value = request.cookies.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
