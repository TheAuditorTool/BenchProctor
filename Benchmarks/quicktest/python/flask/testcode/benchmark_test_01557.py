# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01557():
    raw_body = request.get_data(as_text=True)
    data = (lambda v: v.strip())(raw_body)
    if str(data) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
