# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest63963():
    auth_header = request.headers.get('Authorization', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    def _primary():
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return content
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
