# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
from flask import redirect
import urllib.parse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest43751():
    auth_header = request.headers.get('Authorization', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
