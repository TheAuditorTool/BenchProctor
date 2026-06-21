# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest63643():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '{}'.format(header_value)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
