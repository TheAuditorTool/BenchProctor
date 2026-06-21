# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest38722():
    host_value = request.headers.get('Host', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(host_value)
    data = collected
    return jsonify({'error': 'An internal error occurred'}), 500
