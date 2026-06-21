# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76871():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = ' '.join(str(forwarded_ip).split())
    if str(data) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
