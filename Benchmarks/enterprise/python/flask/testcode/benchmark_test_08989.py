# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest08989():
    origin_value = request.headers.get('Origin', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
