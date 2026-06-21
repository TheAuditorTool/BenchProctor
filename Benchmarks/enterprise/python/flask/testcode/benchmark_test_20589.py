# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20589():
    host_value = request.headers.get('Host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
