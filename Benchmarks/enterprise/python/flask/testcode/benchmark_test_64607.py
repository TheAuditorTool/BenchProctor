# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64607():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    if str(data).endswith(('.prod.internal', '.trusted.net')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
