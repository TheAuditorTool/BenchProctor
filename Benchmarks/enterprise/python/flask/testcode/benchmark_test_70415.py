# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest70415():
    origin_value = request.headers.get('Origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
