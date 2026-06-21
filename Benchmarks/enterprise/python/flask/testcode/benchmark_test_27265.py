# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest27265():
    host_value = request.headers.get('Host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
