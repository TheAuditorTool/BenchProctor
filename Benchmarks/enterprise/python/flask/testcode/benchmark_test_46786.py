# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46786():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value}'
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
