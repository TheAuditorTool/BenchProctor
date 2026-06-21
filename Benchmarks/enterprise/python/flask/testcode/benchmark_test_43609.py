# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest43609():
    header_value = request.headers.get('X-Custom-Header', '')
    size = min(int(header_value) if str(header_value).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
