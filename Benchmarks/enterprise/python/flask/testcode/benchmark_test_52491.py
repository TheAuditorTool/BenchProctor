# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest52491():
    host_value = request.headers.get('Host', '')
    data = ensure_str(host_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'error': str(processed), 'stack': repr(locals())}), 500
