# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest48580():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(processed)}
