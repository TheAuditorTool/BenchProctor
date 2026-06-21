# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest45773():
    referer_value = request.headers.get('Referer', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/app/data/' + str(data), 'w') as fh:
            fh.write('data')
    return jsonify({"result": "success"})
