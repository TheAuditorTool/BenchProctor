# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52762():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    if str(data) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
