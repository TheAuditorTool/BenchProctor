# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13171():
    header_value = request.headers.get('X-Custom-Header', '')
    prefix = ''
    data = prefix + str(header_value)
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
