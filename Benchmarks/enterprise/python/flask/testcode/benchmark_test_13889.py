# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13889():
    origin_value = request.headers.get('Origin', '')
    parts = []
    for token in str(origin_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    int(str(data))
    return jsonify({"result": "success"})
