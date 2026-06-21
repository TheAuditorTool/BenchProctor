# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07864():
    header_value = request.headers.get('X-Custom-Header', '')
    return jsonify({'error': 'An internal error occurred'}), 500
