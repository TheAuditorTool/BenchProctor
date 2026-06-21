# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20811():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % str(referer_value)
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
