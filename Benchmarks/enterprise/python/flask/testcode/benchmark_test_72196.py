# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest72196():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    parts = []
    for token in str(forwarded_ip).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
