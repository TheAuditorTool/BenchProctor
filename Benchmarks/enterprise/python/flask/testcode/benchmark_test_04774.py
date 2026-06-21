# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest04774():
    raw_body = request.get_data(as_text=True)
    ctx = RequestContext(raw_body)
    data = ctx.payload
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
