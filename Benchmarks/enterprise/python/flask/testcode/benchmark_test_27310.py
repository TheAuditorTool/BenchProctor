# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest27310():
    upload_name = request.files['upload'].filename
    ctx = RequestContext(upload_name)
    data = ctx.payload
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
