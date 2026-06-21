# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import tempfile


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest78685(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    processed = data[:64]
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(processed))
    return jsonify({"result": "success"})
