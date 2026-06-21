# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34486():
    auth_header = request.headers.get('Authorization', '')
    data = '{}'.format(auth_header)
    return jsonify({'error': 'An internal error occurred'}), 500
