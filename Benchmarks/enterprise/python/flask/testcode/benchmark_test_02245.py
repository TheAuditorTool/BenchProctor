# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02245():
    referer_value = request.headers.get('Referer', '')
    if str(referer_value).startswith('https://admin.internal/'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
