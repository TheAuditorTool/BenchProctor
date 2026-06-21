# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ctypes


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest03989():
    raw_body = request.get_data(as_text=True)
    ctx = RequestContext(raw_body)
    data = ctx.payload
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
