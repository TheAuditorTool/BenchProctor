# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest06127():
    header_value = request.headers.get('X-Custom-Header', '')
    data = coalesce_blank(header_value)
    return jsonify({'error': 'An internal error occurred'}), 500
