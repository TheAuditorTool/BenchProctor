# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest13325():
    host_value = request.headers.get('Host', '')
    data = default_blank(host_value)
    return jsonify({'error': 'An internal error occurred'}), 500
