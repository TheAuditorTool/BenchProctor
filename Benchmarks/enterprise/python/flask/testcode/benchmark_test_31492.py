# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31492():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    return jsonify({'error': 'An internal error occurred'}), 500
