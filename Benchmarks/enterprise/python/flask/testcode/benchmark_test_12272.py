# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12272():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
