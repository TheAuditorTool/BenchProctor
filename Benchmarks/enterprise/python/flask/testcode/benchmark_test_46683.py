# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46683():
    referer_value = request.headers.get('Referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
