# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39368():
    host_value = request.headers.get('Host', '')
    try:
        result = int(str(host_value))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
