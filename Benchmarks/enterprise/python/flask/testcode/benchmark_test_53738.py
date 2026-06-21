# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53738():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
