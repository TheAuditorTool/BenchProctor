# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05403():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    def normalize(value):
        return value.strip()
    data = normalize(forwarded_ip)
    return jsonify({'error': 'An internal error occurred'}), 500
