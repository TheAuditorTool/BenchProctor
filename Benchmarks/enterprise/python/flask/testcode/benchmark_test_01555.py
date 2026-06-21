# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import defusedxml.ElementTree


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest01555():
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
