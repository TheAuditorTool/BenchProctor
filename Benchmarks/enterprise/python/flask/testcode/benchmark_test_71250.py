# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest71250():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if forwarded_ip not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = forwarded_ip
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
