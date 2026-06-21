# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77807():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
