# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69303():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ' '.join(str(header_value).split())
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
