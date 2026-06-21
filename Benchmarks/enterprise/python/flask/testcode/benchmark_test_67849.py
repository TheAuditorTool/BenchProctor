# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest67849():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % str(auth_header)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
