# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28963():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
