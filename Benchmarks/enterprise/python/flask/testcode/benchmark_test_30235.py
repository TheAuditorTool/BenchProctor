# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest30235():
    upload_name = request.files['upload'].filename
    ctx = RequestContext(upload_name)
    data = ctx.payload
    processed = data[:64]
    os.setuid(int(str(processed)) if str(processed).isdigit() else 0)
    return jsonify({"result": "success"})
