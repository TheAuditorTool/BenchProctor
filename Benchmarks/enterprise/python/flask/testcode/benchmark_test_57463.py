# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import importlib
import sys


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest57463():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
