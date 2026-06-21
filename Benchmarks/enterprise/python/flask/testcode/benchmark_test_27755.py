# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest27755():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % str(auth_header)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
