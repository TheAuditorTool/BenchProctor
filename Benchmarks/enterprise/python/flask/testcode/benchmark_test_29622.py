# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest29622():
    auth_header = request.headers.get('Authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
