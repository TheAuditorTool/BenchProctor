# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80173():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
