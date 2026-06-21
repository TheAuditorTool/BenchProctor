# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11008():
    ua_value = request.headers.get('User-Agent', '')
    parts = []
    for token in str(ua_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
