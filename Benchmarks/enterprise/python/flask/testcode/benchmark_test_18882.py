# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18882():
    origin_value = request.headers.get('Origin', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
