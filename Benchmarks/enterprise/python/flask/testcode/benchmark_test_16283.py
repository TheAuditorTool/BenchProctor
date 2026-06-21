# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16283():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
