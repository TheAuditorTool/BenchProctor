# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68576():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
