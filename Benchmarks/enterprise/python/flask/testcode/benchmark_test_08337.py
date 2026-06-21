# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08337():
    host_value = request.headers.get('Host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
