# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest63822():
    ua_value = request.headers.get('User-Agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
