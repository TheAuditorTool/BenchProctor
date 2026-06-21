# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54901():
    auth_header = request.headers.get('Authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
