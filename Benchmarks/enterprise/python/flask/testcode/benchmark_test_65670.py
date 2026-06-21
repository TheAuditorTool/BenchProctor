# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest65670(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
