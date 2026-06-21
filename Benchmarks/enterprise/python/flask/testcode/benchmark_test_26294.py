# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest26294():
    origin_value = request.headers.get('Origin', '')
    data = '{}'.format(origin_value)
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
