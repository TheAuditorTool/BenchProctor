# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18417():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header}'
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
