# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest30831():
    upload_name = request.files['upload'].filename
    ctx = RequestContext(upload_name)
    data = ctx.payload
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
