# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest12319():
    referer_value = request.headers.get('Referer', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
