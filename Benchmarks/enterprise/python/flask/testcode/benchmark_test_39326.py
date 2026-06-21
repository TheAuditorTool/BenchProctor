# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39326():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
