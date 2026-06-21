# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41991():
    header_value = request.headers.get('X-Custom-Header', '')
    data = bytes.fromhex(header_value).decode('utf-8', 'ignore')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
