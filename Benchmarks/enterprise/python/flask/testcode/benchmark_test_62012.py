# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest62012():
    field_value = request.form.get('field', '')
    data = to_text(field_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
