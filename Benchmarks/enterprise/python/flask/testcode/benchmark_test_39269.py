# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39269():
    origin_value = request.headers.get('Origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
