# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41664():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
