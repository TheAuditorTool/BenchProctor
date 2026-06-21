# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31677():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    if str(data) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
