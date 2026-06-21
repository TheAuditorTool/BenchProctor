# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ctypes


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest31804():
    user_id = request.args.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
