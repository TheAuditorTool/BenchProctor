# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42442():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '{}'.format(header_value)
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
