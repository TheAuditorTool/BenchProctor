# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest48667():
    header_value = request.headers.get('X-Custom-Header', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    checked_path = os.path.normpath(data)
    with open('/var/app/data/' + str(checked_path), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
