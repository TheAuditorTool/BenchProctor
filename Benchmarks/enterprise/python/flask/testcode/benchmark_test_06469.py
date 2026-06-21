# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import unicodedata


def BenchmarkTest06469():
    ua_value = request.headers.get('User-Agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    normalized = unicodedata.normalize('NFKC', str(processed))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
