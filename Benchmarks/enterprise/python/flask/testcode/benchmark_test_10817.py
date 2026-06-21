# SPDX-License-Identifier: Apache-2.0
from flask import session
import re
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest10817():
    header_value = request.headers.get('X-Custom-Header', '')
    data = default_blank(header_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    session['data'] = str(processed)
    return jsonify({"result": "success"})
