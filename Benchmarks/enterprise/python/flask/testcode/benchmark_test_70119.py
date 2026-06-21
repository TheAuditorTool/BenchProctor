# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest70119():
    referer_value = request.headers.get('Referer', '')
    if str(referer_value) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
