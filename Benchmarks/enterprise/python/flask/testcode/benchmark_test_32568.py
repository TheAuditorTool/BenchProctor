# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32568():
    ua_value = request.headers.get('User-Agent', '')
    data = '{}'.format(ua_value)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
