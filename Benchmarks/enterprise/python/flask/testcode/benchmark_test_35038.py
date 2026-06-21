# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35038():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
