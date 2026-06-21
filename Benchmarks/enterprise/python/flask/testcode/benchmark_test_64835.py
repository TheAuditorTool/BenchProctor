# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64835():
    origin_value = request.headers.get('Origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
