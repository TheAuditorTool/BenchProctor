# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33236():
    ua_value = request.headers.get('User-Agent', '')
    data = (lambda v: v.strip())(ua_value)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
