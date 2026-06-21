# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77262():
    auth_header = request.headers.get('Authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    int(str(data))
    return jsonify({"result": "success"})
