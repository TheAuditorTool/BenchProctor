# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09089():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
