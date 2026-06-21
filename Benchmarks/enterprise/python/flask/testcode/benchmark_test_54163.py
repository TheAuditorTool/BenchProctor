# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54163():
    origin_value = request.headers.get('Origin', '')
    if origin_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = origin_value
    return str(processed), 200, {'Content-Type': 'text/html'}
