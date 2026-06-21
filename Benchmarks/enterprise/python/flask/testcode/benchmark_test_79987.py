# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest79987():
    upload_name = request.files['upload'].filename
    ctx = RequestContext(upload_name)
    data = ctx.payload
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
