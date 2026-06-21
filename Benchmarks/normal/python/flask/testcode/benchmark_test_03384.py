# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03384():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    return jsonify({'error': 'An internal error occurred'}), 500
