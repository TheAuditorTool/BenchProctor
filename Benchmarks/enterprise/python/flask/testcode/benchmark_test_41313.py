# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41313():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
