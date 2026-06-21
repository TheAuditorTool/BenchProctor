# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40503():
    header_value = request.headers.get('X-Custom-Header', '')
    if str(header_value).startswith(('10.', '192.168.', '127.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
