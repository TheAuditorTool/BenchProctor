# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02502():
    header_value = request.headers.get('X-Custom-Header', '')
    prefix = ''
    data = prefix + str(header_value)
    return jsonify({'error': 'An internal error occurred'}), 500
