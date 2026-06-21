# SPDX-License-Identifier: Apache-2.0
from flask import request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest38949():
    host_value = request.headers.get('Host', '')
    ctx = RequestContext(host_value)
    data = ctx.payload
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
