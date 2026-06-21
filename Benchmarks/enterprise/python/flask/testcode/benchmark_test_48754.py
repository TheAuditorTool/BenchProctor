# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest48754():
    auth_header = request.headers.get('Authorization', '')
    if auth_header not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = auth_header
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(processed)}
