# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32001():
    header_value = request.headers.get('X-Custom-Header', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(header_value)
    data = collected
    return jsonify({'error': 'An internal error occurred'}), 500
