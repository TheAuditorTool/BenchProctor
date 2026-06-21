# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest67183():
    header_value = request.headers.get('X-Custom-Header', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
