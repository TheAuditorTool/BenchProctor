# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest64259():
    referer_value = request.headers.get('Referer', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return jsonify({"result": "success"})
