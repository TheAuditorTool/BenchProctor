# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest70975():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    processed = str(data).replace("<script", "")
    return Markup('<div>' + str(processed) + '</div>')
