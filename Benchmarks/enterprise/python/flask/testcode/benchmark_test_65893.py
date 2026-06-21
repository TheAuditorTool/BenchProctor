# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65893():
    auth_header = request.headers.get('Authorization', '')
    return jsonify({'error': 'An internal error occurred'}), 500
