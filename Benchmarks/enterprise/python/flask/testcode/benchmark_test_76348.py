# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76348():
    header_value = request.headers.get('X-Custom-Header', '')
    prefix = ''
    data = prefix + str(header_value)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
