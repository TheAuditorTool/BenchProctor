# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25001():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header}'
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
