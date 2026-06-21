# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest36837():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    def _primary():
        return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
