# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest63302():
    host_value = request.headers.get('Host', '')
    parts = []
    for token in str(host_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
