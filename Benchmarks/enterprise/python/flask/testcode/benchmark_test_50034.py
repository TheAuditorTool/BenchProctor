# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest50034():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header}'
    return jsonify({'error': 'An internal error occurred'}), 500
