# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64367():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    parts = str(forwarded_ip).split(',')
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500
