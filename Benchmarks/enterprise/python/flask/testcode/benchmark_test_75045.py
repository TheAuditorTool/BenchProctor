# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import unicodedata


request_state: dict[str, str] = {}

def BenchmarkTest75045():
    auth_header = request.headers.get('Authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    normalized = unicodedata.normalize('NFKC', str(processed))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
