# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13298():
    cookie_value = request.cookies.get('session_token', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(cookie_value)
    data = collected
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
