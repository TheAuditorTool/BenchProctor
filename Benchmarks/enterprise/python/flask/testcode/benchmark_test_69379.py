# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69379():
    auth_header = request.headers.get('Authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
