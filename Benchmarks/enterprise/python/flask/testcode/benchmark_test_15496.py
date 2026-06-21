# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15496():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    if str(data) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
