# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest49160():
    auth_header = request.headers.get('Authorization', '')
    def normalize(value):
        return value.strip()
    data = normalize(auth_header)
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
