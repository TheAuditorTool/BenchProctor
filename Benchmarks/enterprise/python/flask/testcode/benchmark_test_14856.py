# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14856():
    auth_header = request.headers.get('Authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    int(str(data))
    return jsonify({"result": "success"})
