# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18404():
    auth_header = request.headers.get('Authorization', '')
    data = bytearray(int(auth_header) if str(auth_header).isdigit() else 0)
    return jsonify({"result": "success"})
