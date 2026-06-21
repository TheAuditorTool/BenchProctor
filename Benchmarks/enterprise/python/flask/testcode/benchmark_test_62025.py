# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest62025():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
