# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06531():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
