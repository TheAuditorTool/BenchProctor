# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09528():
    origin_value = request.headers.get('Origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    if str(data).startswith('https://admin.internal/'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
