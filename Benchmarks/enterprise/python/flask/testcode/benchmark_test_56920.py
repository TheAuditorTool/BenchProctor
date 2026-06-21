# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56920():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
