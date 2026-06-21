# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest23672():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % (header_value,)
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
