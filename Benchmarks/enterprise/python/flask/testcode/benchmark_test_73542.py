# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest73542():
    referer_value = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
