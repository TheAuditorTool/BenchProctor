# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest38526():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    def _primary():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
