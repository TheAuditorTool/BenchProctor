# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest67548():
    auth_header = request.headers.get('Authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
