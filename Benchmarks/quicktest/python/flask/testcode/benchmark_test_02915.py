# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02915():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = (lambda v: v.strip())(forwarded_ip)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
