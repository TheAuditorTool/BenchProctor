# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request, jsonify
import time


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest53466():
    upload_name = request.files['upload'].filename
    ctx = RequestContext(upload_name)
    data = ctx.payload
    if time.time() > 1000000000:
        return Markup('<img src="' + str(data) + '">')
    return jsonify({"result": "success"})
