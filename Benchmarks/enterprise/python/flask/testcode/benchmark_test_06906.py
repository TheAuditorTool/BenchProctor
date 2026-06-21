# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06906():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
