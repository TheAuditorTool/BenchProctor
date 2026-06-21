# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56651():
    header_value = request.headers.get('X-Custom-Header', '')
    if str(header_value) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
