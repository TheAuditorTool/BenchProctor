# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
import sys
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest01181():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    ctx = RequestContext(argv_value)
    data = ctx.payload
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
