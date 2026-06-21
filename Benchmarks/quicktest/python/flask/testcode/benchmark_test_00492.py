# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00492():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
