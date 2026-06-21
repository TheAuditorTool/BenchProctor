# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65729():
    origin_value = request.headers.get('Origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
