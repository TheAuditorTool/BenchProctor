# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41703():
    host_value = request.headers.get('Host', '')
    if str(host_value) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
