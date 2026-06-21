# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53817():
    host_value = request.headers.get('Host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
