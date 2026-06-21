# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59817():
    auth_header = request.headers.get('Authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
