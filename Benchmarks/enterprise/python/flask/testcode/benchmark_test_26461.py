# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest26461():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ' '.join(str(header_value).split())
    return jsonify({'error': 'An internal error occurred'}), 500
