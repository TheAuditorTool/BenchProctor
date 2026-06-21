# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53272():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
