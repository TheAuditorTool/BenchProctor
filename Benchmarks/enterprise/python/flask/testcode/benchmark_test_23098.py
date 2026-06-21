# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest23098():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    if str(data).startswith('https://admin.internal/'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
