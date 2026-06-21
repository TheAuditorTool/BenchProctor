# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest73094():
    header_value = request.headers.get('X-Custom-Header', '')
    parts = str(header_value).split(',')
    data = ','.join(parts)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
