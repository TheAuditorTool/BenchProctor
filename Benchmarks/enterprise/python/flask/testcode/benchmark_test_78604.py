# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest78604():
    header_value = request.headers.get('X-Custom-Header', '')
    parts = []
    for token in str(header_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
