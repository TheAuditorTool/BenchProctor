# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest74595():
    ua_value = request.headers.get('User-Agent', '')
    try:
        result = int(str(ua_value))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
