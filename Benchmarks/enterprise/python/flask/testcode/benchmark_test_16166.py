# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16166():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
