# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest57589():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % str(header_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
