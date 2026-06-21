# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79129():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % str(header_value)
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
