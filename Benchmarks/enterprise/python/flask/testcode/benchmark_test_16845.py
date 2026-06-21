# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16845():
    origin_value = request.headers.get('Origin', '')
    data = str(origin_value).replace('\x00', '')
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
