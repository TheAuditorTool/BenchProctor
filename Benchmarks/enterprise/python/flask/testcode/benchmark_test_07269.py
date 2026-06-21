# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import tempfile


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest07269():
    host_value = request.headers.get('Host', '')
    ctx = RequestContext(host_value)
    data = ctx.payload
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
