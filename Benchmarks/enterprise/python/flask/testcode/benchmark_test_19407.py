# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19407():
    header_value = request.headers.get('X-Custom-Header', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    if str(data) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
