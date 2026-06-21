# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04504():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
