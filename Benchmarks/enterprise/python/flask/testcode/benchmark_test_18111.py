# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import re
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest18111():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ensure_str(header_value)
    if not re.fullmatch('^[\\w\\s./\\\\:_?&=\\-@]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return redirect(str(processed))
