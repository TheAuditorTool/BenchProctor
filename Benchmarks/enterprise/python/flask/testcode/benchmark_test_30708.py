# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import unicodedata


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest30708():
    upload_name = request.files['upload'].filename
    ctx = RequestContext(upload_name)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    normalized = unicodedata.normalize('NFKC', str(processed))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
