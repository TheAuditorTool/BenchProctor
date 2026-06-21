# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28330():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
