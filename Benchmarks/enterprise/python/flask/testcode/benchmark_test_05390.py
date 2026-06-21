# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05390():
    host_value = request.headers.get('Host', '')
    parts = []
    for token in str(host_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    int(str(data))
    return jsonify({"result": "success"})
