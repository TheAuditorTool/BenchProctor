# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01005():
    ua_value = request.headers.get('User-Agent', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(ua_value)
    data = collected
    return jsonify({'error': 'An internal error occurred'}), 500
