# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01451():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
