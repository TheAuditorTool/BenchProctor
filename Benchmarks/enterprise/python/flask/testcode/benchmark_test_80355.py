# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80355():
    header_value = request.headers.get('X-Custom-Header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
