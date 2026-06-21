# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22512():
    auth_header = request.headers.get('Authorization', '')
    data = (lambda v: v.strip())(auth_header)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
