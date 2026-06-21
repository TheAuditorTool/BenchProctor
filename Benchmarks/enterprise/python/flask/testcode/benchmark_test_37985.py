# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37985():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    return jsonify({'error': 'An internal error occurred'}), 500
