# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53302():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ' '.join(str(header_value).split())
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
