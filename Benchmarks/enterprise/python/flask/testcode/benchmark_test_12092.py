# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12092():
    host_value = request.headers.get('Host', '')
    data = f'{host_value}'
    if str(data).endswith(('.prod.internal', '.trusted.net')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
