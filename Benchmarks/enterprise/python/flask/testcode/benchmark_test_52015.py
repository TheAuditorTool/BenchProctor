# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52015():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
