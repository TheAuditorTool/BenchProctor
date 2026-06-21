# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19670():
    header_value = request.headers.get('X-Custom-Header', '')
    return jsonify({'error': str(header_value), 'stack': repr(locals())}), 500
