# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest36048():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ' '.join(str(header_value).split())
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
