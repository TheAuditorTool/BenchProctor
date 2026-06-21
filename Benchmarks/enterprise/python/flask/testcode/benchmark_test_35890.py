# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35890():
    host_value = request.headers.get('Host', '')
    if str(host_value) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
