# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest05798():
    upload_name = request.files['upload'].filename
    ctx = RequestContext(upload_name)
    data = ctx.payload
    return render_template_string('safe block: {{ value }}', value=data)
