# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest31014(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
