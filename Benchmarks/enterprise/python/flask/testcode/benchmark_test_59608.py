# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59608():
    ua_value = request.headers.get('User-Agent', '')
    data = (lambda v: v.strip())(ua_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
