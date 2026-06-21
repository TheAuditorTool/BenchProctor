# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest74183():
    origin_value = request.headers.get('Origin', '')
    try:
        result = int(str(origin_value))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
