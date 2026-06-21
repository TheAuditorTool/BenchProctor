# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76318():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip}'
    return jsonify({'error': 'An internal error occurred'}), 500
