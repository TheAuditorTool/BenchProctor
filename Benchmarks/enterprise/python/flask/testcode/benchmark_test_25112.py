# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25112():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % str(referer_value)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
