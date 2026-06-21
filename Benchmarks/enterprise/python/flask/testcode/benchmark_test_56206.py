# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56206():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return str(processed), 200, {'Content-Type': 'text/html'}
