# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20628():
    auth_header = request.headers.get('Authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
