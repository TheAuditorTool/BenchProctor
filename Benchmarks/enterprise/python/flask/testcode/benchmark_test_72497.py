# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest72497():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
