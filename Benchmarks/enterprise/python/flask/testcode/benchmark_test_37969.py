# SPDX-License-Identifier: Apache-2.0
import os
import sys
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest37969():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    ctx = RequestContext(argv_value)
    data = ctx.payload
    processed = data[:64]
    os.unlink('/var/app/data/' + str(processed))
    return jsonify({"result": "success"})
