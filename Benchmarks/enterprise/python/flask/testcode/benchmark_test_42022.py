# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest42022(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    os.remove(str(data))
    return jsonify({"result": "success"})
