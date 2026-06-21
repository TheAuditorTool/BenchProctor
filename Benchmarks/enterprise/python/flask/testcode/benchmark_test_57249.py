# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest57249():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
