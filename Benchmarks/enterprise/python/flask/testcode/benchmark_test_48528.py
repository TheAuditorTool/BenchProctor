# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest48528():
    header_value = request.headers.get('X-Custom-Header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    return jsonify({'error': 'An internal error occurred'}), 500
