# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest17849():
    header_value = request.headers.get('X-Custom-Header', '')
    data = default_blank(header_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
