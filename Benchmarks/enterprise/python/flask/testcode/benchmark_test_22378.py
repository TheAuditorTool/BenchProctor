# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22378():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
