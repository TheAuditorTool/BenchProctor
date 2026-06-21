# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest69035():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = (lambda v: v.strip())(forwarded_ip)
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
