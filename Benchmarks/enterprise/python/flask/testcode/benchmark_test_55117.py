# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest55117():
    host_value = request.headers.get('Host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
