# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14802():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
