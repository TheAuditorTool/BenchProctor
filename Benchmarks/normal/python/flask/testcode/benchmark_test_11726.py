# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest11726():
    ua_value = request.headers.get('User-Agent', '')
    ctx = RequestContext(ua_value)
    data = ctx.payload
    auth_check('user', data)
    return jsonify({"result": "success"})
