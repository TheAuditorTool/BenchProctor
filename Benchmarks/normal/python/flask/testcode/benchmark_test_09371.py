# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09371():
    header_value = request.headers.get('X-Custom-Header', '')
    data = (lambda v: v.strip())(header_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
