# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33668():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
