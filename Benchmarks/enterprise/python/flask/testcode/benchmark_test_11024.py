# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11024():
    cookie_value = request.cookies.get('session_token', '')
    parts = []
    for token in str(cookie_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500
