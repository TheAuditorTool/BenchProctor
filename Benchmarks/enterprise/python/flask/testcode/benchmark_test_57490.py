# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest57490():
    ua_value = request.headers.get('User-Agent', '')
    if str(ua_value) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
