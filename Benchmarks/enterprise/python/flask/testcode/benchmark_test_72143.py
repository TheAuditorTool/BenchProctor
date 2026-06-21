# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72143():
    cookie_value = request.cookies.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
