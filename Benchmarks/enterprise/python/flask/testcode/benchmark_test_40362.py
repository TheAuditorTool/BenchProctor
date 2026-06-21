# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40362():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value}'
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
