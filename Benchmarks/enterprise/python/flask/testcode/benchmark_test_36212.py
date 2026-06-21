# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest36212():
    ua_value = request.headers.get('User-Agent', '')
    data = (lambda v: v.strip())(ua_value)
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
