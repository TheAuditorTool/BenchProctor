# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20972():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
