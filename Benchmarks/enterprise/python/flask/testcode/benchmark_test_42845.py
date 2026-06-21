# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import re
from flask import request, jsonify


def BenchmarkTest42845():
    header_value = request.headers.get('X-Custom-Header', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(header_value)
    data = collected
    if not re.fullmatch('^[\\w\\s./\\\\:_?&=\\-@]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return redirect(str(processed))
