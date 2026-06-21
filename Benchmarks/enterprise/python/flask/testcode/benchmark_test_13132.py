# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13132():
    origin_value = request.headers.get('Origin', '')
    if str(origin_value) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
