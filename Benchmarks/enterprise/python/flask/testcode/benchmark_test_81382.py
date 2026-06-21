# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import importlib


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest81382():
    field_value = request.form.get('field', '')
    ctx = RequestContext(field_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        importlib.import_module(str(data))
    return jsonify({"result": "success"})
