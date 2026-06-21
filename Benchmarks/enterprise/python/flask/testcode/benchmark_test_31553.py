# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
from flask import render_template_string


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest31553():
    user_id = request.args.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    return render_template_string('{{ value }}', value=data)
