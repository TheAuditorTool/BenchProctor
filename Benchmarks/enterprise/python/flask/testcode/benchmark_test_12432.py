# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12432():
    ua_value = request.headers.get('User-Agent', '')
    data = (lambda v: v.strip())(ua_value)
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
