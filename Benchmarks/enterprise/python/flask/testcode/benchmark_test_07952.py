# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest07952(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
