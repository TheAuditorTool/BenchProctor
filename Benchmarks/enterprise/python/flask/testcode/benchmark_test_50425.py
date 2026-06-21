# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest50425():
    host_value = request.headers.get('Host', '')
    data = '%s' % (host_value,)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
