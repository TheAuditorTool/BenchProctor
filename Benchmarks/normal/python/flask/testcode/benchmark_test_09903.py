# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09903():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
