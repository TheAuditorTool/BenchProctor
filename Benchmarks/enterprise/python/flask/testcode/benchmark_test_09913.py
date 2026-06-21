# SPDX-License-Identifier: Apache-2.0
import jwt
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest09913():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    ctx = RequestContext(secret_value)
    data = ctx.payload
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return jsonify({"result": "success"})
