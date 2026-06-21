# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72169():
    auth_header = request.headers.get('Authorization', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(auth_header)
    data = collected
    return jsonify({'error': 'An internal error occurred'}), 500
