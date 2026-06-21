# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59071():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % str(ua_value)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
