# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest38862():
    host_value = request.headers.get('Host', '')
    ctx = RequestContext(host_value)
    data = ctx.payload
    processed = data[:64]
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
