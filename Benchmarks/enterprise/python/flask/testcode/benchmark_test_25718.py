# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25718():
    header_value = request.headers.get('X-Custom-Header', '')
    parts = str(header_value).split(',')
    data = ','.join(parts)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
