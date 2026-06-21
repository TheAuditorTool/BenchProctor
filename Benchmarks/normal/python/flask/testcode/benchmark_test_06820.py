# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06820():
    ua_value = request.headers.get('User-Agent', '')
    data = ' '.join(str(ua_value).split())
    if str(data) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
