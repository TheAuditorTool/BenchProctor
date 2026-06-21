# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51202():
    auth_header = request.headers.get('Authorization', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    return jsonify({'error': 'An internal error occurred'}), 500
