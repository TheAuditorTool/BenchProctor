# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11440():
    referer_value = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
