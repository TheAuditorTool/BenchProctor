# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest37468():
    multipart_value = request.form.get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    def _primary():
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return content
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
