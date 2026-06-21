# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest06208():
    user_id = request.args.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    os.seteuid(65534)
    return jsonify({"result": "success"})
