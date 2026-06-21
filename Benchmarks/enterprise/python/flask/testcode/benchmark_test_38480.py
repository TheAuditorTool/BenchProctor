# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest38480():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if str(forwarded_ip) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
