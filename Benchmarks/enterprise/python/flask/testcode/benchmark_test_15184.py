# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest15184():
    host_value = request.headers.get('Host', '')
    ctx = RequestContext(host_value)
    data = ctx.payload
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
