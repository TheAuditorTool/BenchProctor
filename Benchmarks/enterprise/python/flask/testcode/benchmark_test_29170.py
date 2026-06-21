# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest29170(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    session['user'] = str(data)
    return jsonify({"result": "success"})
