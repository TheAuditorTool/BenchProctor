# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58271():
    origin_value = request.headers.get('Origin', '')
    size = min(int(origin_value) if str(origin_value).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
