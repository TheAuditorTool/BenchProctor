# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19753():
    origin_value = request.headers.get('Origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
