# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest57854():
    cookie_value = request.cookies.get('session_token', '')
    ctx = RequestContext(cookie_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
