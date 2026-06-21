# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib
import sys


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest01597(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    eval(compile("sys.path.insert(0, str(data))\nimportlib.import_module('report_renderer')", '<sink>', 'exec'))
    return jsonify({"result": "success"})
