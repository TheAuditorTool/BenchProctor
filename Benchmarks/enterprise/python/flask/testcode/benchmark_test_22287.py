# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22287():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip:.200s}'
    return jsonify({'error': 'An internal error occurred'}), 500
