# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08385():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = ' '.join(str(forwarded_ip).split())
    return jsonify({'error': 'An internal error occurred'}), 500
