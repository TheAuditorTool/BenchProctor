# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest43833():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = (lambda v: v.strip())(forwarded_ip)
    return jsonify({'error': 'An internal error occurred'}), 500
