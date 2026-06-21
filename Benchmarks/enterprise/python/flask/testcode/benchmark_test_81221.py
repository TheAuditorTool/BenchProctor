# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest81221():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
