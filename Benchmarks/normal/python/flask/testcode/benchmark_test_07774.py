# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07774():
    auth_header = request.headers.get('Authorization', '')
    data = (lambda v: v.strip())(auth_header)
    return jsonify({'error': 'An internal error occurred'}), 500
