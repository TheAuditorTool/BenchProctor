# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60874():
    header_value = request.headers.get('X-Custom-Header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
