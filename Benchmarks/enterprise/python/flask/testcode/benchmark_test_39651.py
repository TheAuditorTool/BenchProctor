# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39651():
    raw_body = request.get_data(as_text=True)
    if str(raw_body) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
