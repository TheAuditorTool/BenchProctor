# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest26033():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
