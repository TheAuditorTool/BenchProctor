# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61889():
    raw_body = request.get_data(as_text=True)
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(raw_body)
    data = collected
    return jsonify({'error': 'An internal error occurred'}), 500
