# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01288():
    auth_header = request.headers.get('Authorization', '')
    try:
        result = int(str(auth_header))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
