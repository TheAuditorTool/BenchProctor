# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46041():
    auth_header = request.headers.get('Authorization', '')
    size = min(int(auth_header) if str(auth_header).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
