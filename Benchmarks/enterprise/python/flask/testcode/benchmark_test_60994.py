# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest60994():
    cookie_value = request.cookies.get('session_token', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(cookie_value)
    data = collected
    if not re.fullmatch('^[\\w\\s.\\-:/=\\r\\n]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return '<html><body><h1>' + str(processed) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
