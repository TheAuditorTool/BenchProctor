# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40938():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
