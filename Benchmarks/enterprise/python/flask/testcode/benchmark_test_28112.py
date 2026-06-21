# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28112():
    auth_header = request.headers.get('Authorization', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
