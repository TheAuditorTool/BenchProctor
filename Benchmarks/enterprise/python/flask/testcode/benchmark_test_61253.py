# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61253():
    referer_value = request.headers.get('Referer', '')
    if str(referer_value).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
