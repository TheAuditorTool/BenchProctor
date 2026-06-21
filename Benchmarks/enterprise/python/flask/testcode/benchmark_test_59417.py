# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify
import time


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest59417():
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    if time.time() > 1000000000:
        requests.get(str(data))
    return jsonify({"result": "success"})
