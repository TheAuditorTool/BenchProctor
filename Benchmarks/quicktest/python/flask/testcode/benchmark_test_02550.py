# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest02550():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
