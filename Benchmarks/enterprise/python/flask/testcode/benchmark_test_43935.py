# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest43935():
    header_value = request.headers.get('X-Custom-Header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
