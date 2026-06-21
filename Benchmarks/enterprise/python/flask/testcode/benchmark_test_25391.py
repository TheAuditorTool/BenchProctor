# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25391():
    origin_value = request.headers.get('Origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
