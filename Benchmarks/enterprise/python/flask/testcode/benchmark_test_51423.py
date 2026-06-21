# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51423():
    origin_value = request.headers.get('Origin', '')
    parts = []
    for token in str(origin_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
