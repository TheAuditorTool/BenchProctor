# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08704():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % (header_value,)
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
