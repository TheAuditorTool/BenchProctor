# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest50310():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
