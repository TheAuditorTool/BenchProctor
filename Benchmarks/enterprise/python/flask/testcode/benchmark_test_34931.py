# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34931():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
