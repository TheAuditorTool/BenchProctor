# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64079():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
