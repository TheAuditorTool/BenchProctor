# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest29574():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    return jsonify({'error': 'An internal error occurred'}), 500
