# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60184():
    header_value = request.headers.get('X-Custom-Header', '')
    data = (lambda v: v.strip())(header_value)
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
