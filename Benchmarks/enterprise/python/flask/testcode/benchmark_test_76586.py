# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request, jsonify
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest76586():
    multipart_value = request.form.get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        return redirect(str(data))
    return jsonify({"result": "success"})
