# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest55119():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
