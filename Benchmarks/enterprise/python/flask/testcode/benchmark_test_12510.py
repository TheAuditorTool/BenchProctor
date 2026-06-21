# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import socket


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest12510():
    header_value = request.headers.get('X-Custom-Header', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        s = socket.create_connection((str(data), 80))
        s.close()
    return jsonify({"result": "success"})
