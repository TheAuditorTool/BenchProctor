# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest27710():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
