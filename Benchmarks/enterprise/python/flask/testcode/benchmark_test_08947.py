# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08947():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ' '.join(str(header_value).split())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
