# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest31679():
    raw_body = request.get_data(as_text=True)
    data = default_blank(raw_body)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    if str(processed) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
