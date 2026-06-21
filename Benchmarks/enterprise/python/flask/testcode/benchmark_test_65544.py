# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65544():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
