# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03076():
    header_value = request.headers.get('X-Custom-Header', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
