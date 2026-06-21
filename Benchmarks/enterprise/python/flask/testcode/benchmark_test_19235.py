# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest19235():
    user_id = request.args.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
