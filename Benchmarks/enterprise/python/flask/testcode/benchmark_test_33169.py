# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33169():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
