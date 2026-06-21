# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest14346():
    cookie_value = request.cookies.get('session_token', '')
    ctx = RequestContext(cookie_value)
    data = ctx.payload
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
