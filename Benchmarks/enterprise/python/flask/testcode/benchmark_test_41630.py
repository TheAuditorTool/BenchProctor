# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41630():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
