# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20339():
    auth_header = request.headers.get('Authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    return jsonify({'error': 'An internal error occurred'}), 500
