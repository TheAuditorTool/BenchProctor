# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40306():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % (origin_value,)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
