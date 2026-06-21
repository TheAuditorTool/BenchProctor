# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01091():
    header_value = request.headers.get('X-Custom-Header', '')
    data = str(header_value).replace('\x00', '')
    return jsonify({'error': 'An internal error occurred'}), 500
