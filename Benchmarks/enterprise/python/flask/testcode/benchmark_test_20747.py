# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20747():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
