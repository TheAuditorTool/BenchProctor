# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import unicodedata


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest00791():
    raw_body = request.get_data(as_text=True)
    ctx = RequestContext(raw_body)
    data = ctx.payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    normalized = unicodedata.normalize('NFKC', str(processed))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
