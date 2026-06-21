# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59330():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip}'
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
