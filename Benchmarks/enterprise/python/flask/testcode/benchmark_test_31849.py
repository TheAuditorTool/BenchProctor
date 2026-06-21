# SPDX-License-Identifier: Apache-2.0
import yaml
import os
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest31849():
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    yaml.safe_load(data)
    return jsonify({"result": "success"})
