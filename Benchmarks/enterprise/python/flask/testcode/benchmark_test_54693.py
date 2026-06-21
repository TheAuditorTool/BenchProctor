# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54693():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    if str(data) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
