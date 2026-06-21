# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest57983():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % str(header_value)
    if str(data).startswith(('10.', '192.168.', '127.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
