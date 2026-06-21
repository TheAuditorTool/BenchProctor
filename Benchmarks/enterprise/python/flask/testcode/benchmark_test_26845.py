# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest26845():
    header_value = request.headers.get('X-Custom-Header', '')
    data = bytes.fromhex(header_value).decode('utf-8', 'ignore')
    return jsonify({'error': 'An internal error occurred'}), 500
