# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest25370():
    referer_value = request.headers.get('Referer', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    processed = str(data).replace("<script", "")
    return Markup('<div>' + str(processed) + '</div>')
