# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05209():
    auth_header = request.headers.get('Authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
