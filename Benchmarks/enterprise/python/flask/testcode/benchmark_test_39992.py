# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39992():
    origin_value = request.headers.get('Origin', '')
    if str(origin_value).startswith('https://admin.internal/'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
