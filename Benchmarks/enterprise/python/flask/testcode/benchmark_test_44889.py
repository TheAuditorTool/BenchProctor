# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import time


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest44889():
    upload_name = request.files['upload'].filename
    ctx = RequestContext(upload_name)
    data = ctx.payload
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return jsonify({"result": "success"})
