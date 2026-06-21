# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest76635():
    header_value = request.headers.get('X-Custom-Header', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(header_value)
    data = collected
    if not re.fullmatch('^[\\w\\s.\\-:/=\\r\\n]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return '<html><body><h1>' + str(processed) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
