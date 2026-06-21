# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
from app_runtime import auth_check


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest26511(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
