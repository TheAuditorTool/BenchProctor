# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08237():
    origin_value = request.headers.get('Origin', '')
    prefix = ''
    data = prefix + str(origin_value)
    if str(data).startswith('https://admin.internal/'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
