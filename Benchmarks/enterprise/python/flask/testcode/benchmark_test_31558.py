# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31558():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '{}'.format(header_value)
    if str(data).startswith(('10.', '192.168.', '127.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
