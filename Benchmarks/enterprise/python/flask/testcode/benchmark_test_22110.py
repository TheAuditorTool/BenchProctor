# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22110():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
