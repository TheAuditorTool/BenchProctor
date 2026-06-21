# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest71353():
    header_value = request.headers.get('X-Custom-Header', '')
    data = (lambda v: v.strip())(header_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
