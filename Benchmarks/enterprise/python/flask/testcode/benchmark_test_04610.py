# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest04610():
    upload_name = request.files['upload'].filename
    data = to_text(upload_name)
    if not re.fullmatch('^[\\w\\s.\\-:/=\\r\\n]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
