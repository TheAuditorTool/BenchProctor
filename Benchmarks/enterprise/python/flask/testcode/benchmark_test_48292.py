# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest48292():
    referer_value = request.headers.get('Referer', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(referer_value)
    data = collected
    return jsonify({'error': 'An internal error occurred'}), 500
