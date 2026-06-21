# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72767():
    auth_header = request.headers.get('Authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500
