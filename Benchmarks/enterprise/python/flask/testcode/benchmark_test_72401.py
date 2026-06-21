# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest72401():
    cookie_value = request.cookies.get('session_token', '')
    data = default_blank(cookie_value)
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
