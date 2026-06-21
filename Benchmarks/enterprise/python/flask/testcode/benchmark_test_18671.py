# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18671():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
