# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest40125():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
