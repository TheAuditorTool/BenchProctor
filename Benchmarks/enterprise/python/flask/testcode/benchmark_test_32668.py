# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32668():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    return jsonify({'error': 'An internal error occurred'}), 500
