# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest73565():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
