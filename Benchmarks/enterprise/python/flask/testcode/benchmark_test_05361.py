# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05361():
    header_value = request.headers.get('X-Custom-Header', '')
    prefix = ''
    data = prefix + str(header_value)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
