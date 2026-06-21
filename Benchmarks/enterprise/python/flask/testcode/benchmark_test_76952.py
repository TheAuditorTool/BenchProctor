# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest76952():
    cookie_value = request.cookies.get('session_token', '')
    ctx = RequestContext(cookie_value)
    data = ctx.payload
    def _primary():
        link_path = os.path.join('/var/app/data', str(data))
        target = os.readlink(link_path)
        with open(target, 'r') as fh:
            content = fh.read()
        return content
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
