# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13182():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
