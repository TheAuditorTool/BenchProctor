# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68462():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    return jsonify({'error': 'An internal error occurred'}), 500
