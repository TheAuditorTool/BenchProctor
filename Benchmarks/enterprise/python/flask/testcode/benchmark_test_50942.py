# SPDX-License-Identifier: Apache-2.0
import tempfile
from flask import request, jsonify
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest50942():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
