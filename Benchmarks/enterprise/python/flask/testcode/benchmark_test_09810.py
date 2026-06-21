# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09810():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % str(auth_header)
    return jsonify({'error': 'An internal error occurred'}), 500
