# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24299():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(forwarded_ip)
    data = collected
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
