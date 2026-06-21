# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25138():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
