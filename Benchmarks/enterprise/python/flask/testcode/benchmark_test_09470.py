# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09470():
    header_value = request.headers.get('X-Custom-Header', '')
    parts = []
    for token in str(header_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
