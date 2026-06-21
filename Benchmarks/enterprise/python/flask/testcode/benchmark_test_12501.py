# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12501():
    header_value = request.headers.get('X-Custom-Header', '')
    if header_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = header_value
    return str(processed), 200, {'Content-Type': 'text/html'}
