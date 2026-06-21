# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import unicodedata


def BenchmarkTest17737():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    normalized = unicodedata.normalize('NFKC', str(processed))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
