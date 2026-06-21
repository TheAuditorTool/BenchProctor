# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08527():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(forwarded_ip)
    data = collected
    return jsonify({'error': 'An internal error occurred'}), 500
