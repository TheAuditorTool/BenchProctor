# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58767():
    auth_header = request.headers.get('Authorization', '')
    def normalize(value):
        return value.strip()
    data = normalize(auth_header)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
