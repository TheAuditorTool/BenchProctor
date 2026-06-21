# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11751():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip}'
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
