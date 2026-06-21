# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest36571():
    host_value = request.headers.get('Host', '')
    data = f'{host_value}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
