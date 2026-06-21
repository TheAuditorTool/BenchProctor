# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30177():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
