# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80777():
    auth_header = request.headers.get('Authorization', '')
    def normalize(value):
        return value.strip()
    data = normalize(auth_header)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
