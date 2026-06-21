# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32264():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '{}'.format(header_value)
    return jsonify({'error': 'An internal error occurred'}), 500
