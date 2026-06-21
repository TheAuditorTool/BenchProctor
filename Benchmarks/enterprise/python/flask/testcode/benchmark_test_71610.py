# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest71610():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % (auth_header,)
    return jsonify({'error': 'An internal error occurred'}), 500
