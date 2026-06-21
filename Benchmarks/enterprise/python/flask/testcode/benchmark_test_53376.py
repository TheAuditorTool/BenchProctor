# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest53376():
    user_id = request.args.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    session['data'] = str(data)
    return jsonify({"result": "success"})
