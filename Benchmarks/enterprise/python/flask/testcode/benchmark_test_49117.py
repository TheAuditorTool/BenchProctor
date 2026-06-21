# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49117():
    auth_header = request.headers.get('Authorization', '')
    if str(auth_header) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
