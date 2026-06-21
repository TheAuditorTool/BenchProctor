# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60085():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
