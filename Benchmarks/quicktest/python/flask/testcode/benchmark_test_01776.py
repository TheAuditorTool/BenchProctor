# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest01776():
    origin_value = request.headers.get('Origin', '')
    data = normalise_input(origin_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
