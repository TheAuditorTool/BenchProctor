# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest02602():
    auth_header = request.headers.get('Authorization', '')
    parts = []
    for token in str(auth_header).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
