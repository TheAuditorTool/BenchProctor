# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest51355(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
