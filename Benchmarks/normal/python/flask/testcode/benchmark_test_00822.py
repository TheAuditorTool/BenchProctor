# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00822():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % (header_value,)
    if str(data) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
